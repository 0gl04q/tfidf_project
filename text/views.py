from django.shortcuts import render
from .forms import FileForm
from text.service.file_manager import add_words_in_file, tf_tdi


def upload_file(request):
    """ Функция отображения загрузки файла """

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)

            # Передаем сырой и сохраненный файл
            add_words_in_file(request.FILES['file'], file)

            return render(request, template_name='word_list.html', context={'word_list': tf_tdi(file)})

    form = FileForm()
    return render(request, template_name='upload_file.html', context={'form': form})
