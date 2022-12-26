from django.urls import path
from .views import LibraryListView, LibraryCreateView, LibraryDetailView
urlpatterns = [
    path('', LibraryListView.as_view(), name='home'),
    path('books/new/', LibraryCreateView.as_view(), name='post_new'), 
    path('books/<int:pk>/', LibraryDetailView.as_view(), name='post_detail'),
]