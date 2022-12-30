from django.urls import path
from . import views
from .views import LibraryCreateView,LibraryUpdateView,LibraryDeleteView
urlpatterns = [
    path('books/new/',  LibraryCreateView.as_view(), name='books_new'), 
    path('books/<int:category>/<int:pk>/', views.LibraryBook, name='books_detail'),
    path('books/<int:category>/', views.LibraryList, name='books_list'),
    path('books/<int:category>/<int:pk>/del/', LibraryDeleteView.as_view()),
    path('books/<int:category>/<int:pk>/patch/', LibraryUpdateView.as_view()),
]