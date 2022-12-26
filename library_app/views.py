from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView 
from .models import Books


def LibraryList(request,category):
    books = Books.objects.filter(Category=category)
    return render(request, 'home.html',{'books':books})

class LibraryDetailView(DetailView):
    model = Books
    template_name = 'books_detail.html'

class LibraryCreateView(CreateView):
    model = Books
    template_name = 'books_new.html'
    fields = ["__all__"]
