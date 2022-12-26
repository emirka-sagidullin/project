from django.urls import path
from . import views
from .views import LibraryCreateView, LibraryDetailView
urlpatterns = [
    path('books/', views.Books)
    path('books/new/', LibraryCreateView.as_view(), name='books_new'), 
    path('books/<str:category>/<int:pk>/', LibraryDetailView.as_view(), name='books_detail'),
    path('books/<str:category>/', views.LibraryList, name='books_list'),
]