from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

# jei norime perduoti papildoma konteksta
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['papildoma'] = 'Sveiki atvyke!!!'
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreatView(CreateView):
    model = Post
    fields = ['title', 'author', 'description']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')
# 'post_list'- tai path i urls.py


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'description']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')