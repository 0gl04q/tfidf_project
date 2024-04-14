from text.models import Word, File
from string import punctuation
import math


def add_words_in_file(file_in_request, file_in_db):
    """ Функция добавления уникальных слов для файла """

    # Преобразуем сырой файл в текст и сохраняем в экземпляре файла
    file_in_db.text = ''.join(chunk.decode('UTF-8') for chunk in file_in_request.chunks())

    # Убираем символы из текста
    text_no_symbol = file_in_db.text.translate(str.maketrans('', '', punctuation))

    # Разбиваем текст на список слов
    split_text = text_no_symbol.split()

    # Находим количество слов файла и сохраняем
    file_in_db.count = len(split_text)
    file_in_db.save()

    # Получаем уникальные слова
    unique_word = set(word.lower() for word in split_text)

    # Отбираем слова для создания, так как в базе могут быть повторения
    words_to_create = [Word(name=word) for word in unique_word if not Word.objects.filter(name=word).exists()]

    # Создаем отобранные слова
    Word.objects.bulk_create(words_to_create)

    # Находим все уникальные слова файла и крепим к файлу
    words_to_add = Word.objects.filter(name__in=unique_word)
    file_in_db.word_set.add(*words_to_add)


def tf_tdi(file):
    """ Функция подсчета tf и tdi """

    # Находим все слова файла
    words = file.word_set.all()

    # Считаем общее количество файлов
    count_all_file = File.objects.count()

    # Возвращаем список словарей с именем, tf и idf
    # tf высчитываем находя количество конкретного слова и делим на общее количество слов в файле
    # idf высчитываем логарифмом деля общее количество файлов на количество всех файлов в которых есть слово
    # Тут так же применяем сортировку по idf в обратном порядке и ограничиваем количество до 50.
    return sorted(({'name': word.name,
                    'tf': file.text.count(word.name) / file.count,
                    'idf': math.log(count_all_file / File.objects.filter(word=word).count())} for word in words),
                  key=lambda x: x['idf'], reverse=True)[:50]
