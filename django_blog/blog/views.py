from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from .models import Post


# 🧩 User Registration
def register_view(request):
    if request.user.is_authenticated:
        return redirect('blog:profile')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            messages.success(request, "Registration successful. Welcome!")
            return redirect('blog:profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form})


# 👤 Profile View and Update
@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('blog:profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {'u_form': u_form, 'p_form': p_form})


# 📝 Blog Post Views (CRUD)
# 1️⃣ List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # template file: blog/home.html
    context_object_name = 'posts'


# 2️⃣ Detail view (single post)
class PostDetailView(DetailView):
    model = Post


# 3️⃣ Create new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created successfully!")
        return super().form_valid(form)


# 4️⃣ Update existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post updated successfully!")
        return super().form_valid(form)

    # Only allow the author to edit
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# 5️⃣ Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
