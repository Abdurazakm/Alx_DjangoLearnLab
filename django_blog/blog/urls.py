# blog/urls.py
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register_view,
    profile_view
)
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    # Blog post URLs
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),  # ✅ CREATE
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # ✅ READ
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # ✅ UPDATE
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # ✅ DELETE

    # Authentication and profile
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]
