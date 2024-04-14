from django import forms

from text.models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].label = ''
