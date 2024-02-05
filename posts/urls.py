from django.urls import path

from posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView, Posts
)

urlpatterns = [
    path('post/create/', PostCreateView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view()),
    path('post/', PostListView.as_view()),
    path('test/', Posts.as_view()),
]
