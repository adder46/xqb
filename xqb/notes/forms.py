from django import forms

from notebooks.models import Notebook
from notes.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'notebook', 'tags']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['notebook'].queryset = Notebook.objects.filter(added_by=user)
