from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Books
from django.urls import reverse_lazy





def LibraryList(request,category):
    books = Books.objects.filter(Category=category)
    return render(request, 'home.html',{'books':books})
    
def LibraryBook(request,category,pk):
    books = Books.objects.filter(Category=category)
    book = books[pk]
    return render(request,'books_detail.html',{'book':book})



class LibraryCreateView(CreateView):
    model = Books
    template_name = 'books_new.html'
    fields = '__all__'

class LibraryUpdateView(UpdateView):
    model = Books
    fields = '__all__'
    template_name_suffix = '_update_form'

class LibraryDeleteView(DeleteView):
    model = Books
    success_url = reverse_lazy('books_list')

