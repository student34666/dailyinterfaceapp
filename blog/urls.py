from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView)

urlpatterns  = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path(
            "favicon.ico",
            RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
        ),
]
