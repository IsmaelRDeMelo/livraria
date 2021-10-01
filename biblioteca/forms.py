from django import forms
from biblioteca.models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
