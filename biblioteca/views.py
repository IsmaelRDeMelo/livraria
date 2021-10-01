from django.db.models import query
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from livraria import biblioteca

from livraria.biblioteca.models import Livro

class LivroList(ListView):
    model = Livro
    queryset = Livro.objects.all()
    
class LivroCreate(CreateView):
    model = Livro
    fields = '__all__'
    success_url = reverse_lazy('biblioteca:list')

class LivroUpdate(UpdateView):
    model = Livro
    fields = '__all__'
    success_url = reverse_lazy('biblioteca:list')

class LivroDetail(DetailView):
    queryset = Livro.objects.all()

class LivroDelete(DeleteView):
    queryset = Livro.objects.all()
    success_url = reverse_lazy('biblioteca:list')
