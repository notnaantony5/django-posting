from django.urls import path

from posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    path('post/create/', PostCreateView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view()),
    path('post/', PostListView.as_view())
]
