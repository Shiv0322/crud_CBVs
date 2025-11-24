from django.urls import path
from .views import *

urlpatterns = [
   
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/add/', AuthorCreateView.as_view(), name='author_add'),
    path('authors/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_edit'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),

  
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/add/', PostCreateView.as_view(), name='post_add'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
