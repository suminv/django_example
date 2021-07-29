from django import forms
from app_media.models import File


class DocumentForm(forms.Form):
    class Meta:
        model = File
        fields = ('description', 'file', )

class MultiFilesForm(forms.Form):
    """
    Загрузка нескольких файлов сразу.
    """

    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    