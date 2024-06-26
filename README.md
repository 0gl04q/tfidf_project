# Тестовое задание по TF-IDF

![image](https://github.com/0gl04q/tfidf_project/assets/115027096/193e0306-bb82-477b-a11f-fa7044facdd1)

Это веб-приложение позволяет загружать текстовые файлы, а затем анализировать их с использованием метода TF-IDF. После обработки файла приложение отображает таблицу с 50 наиболее значимыми словами из текста.
Анализ производится на основе всех загруженных файлов (в задании не была конкретно указана коллекция).

## Описание проекта

### Функциональность

- Страница с формой для загрузки текстового файла.
- Обработка загруженного файла для определения TF-IDF для каждого слова.
- Отображение результатов в виде таблицы, отсортированной по убыванию значения IDF.

### Технологии

- **Фронтенд:** HTML, CSS, HTMX, Bootstrap 5
- **Бэкенд:** Python с использованием фреймворка Django

### Установка и запуск

1. Клонируйте репозиторий: `git clone https://github.com/0gl04q/tfidf_project.git`
2. Установите зависимости: `pip install -r requirements.txt`
