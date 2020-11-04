from django.shortcuts import render
from everydayBlog.models import Post, Comments
from everydayBlog.forms import PostForm, CommentsForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'everydayBlog/about.html'

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model =Post

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name='everydayBlog/detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name='everydayBlog/detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model =Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url='/login/'
    redirect_field_name='everydayBlog/post_list.html'
    model =Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')
