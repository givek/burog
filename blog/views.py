from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import Post, User


@login_required
def profile(request, pk):
    user = User.objects.get(id=pk)
    posts = Post.objects.filter(author=user)
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'blog/profile.html', context)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'thumbnail', 'content', 'overview']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'thumbnail', 'content', 'overview']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def is_post_author(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def is_post_author(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
