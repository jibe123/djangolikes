from django.urls import path
from .views import (
    post_list_view,
    post_create_view,
    post_detail_view,
    like_view
)

urlpatterns = [
    path('posts/', post_list_view, name='post-list'),
    path('posts/create/', post_create_view, name='post-create'),
    path('posts/<int:id>/', post_detail_view, name='post-detail'),
    path('posts/like/<int:id>/', like_view, name='post-like'),
]