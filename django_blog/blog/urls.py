from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 🏠 Home & Profile
    path('', views.PostListView.as_view(), name='home'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # 📝 Post CRUD
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # 💬 Comment CRUD (linked to specific posts)
    path('post/<int:pk>/comment/new/', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
]
