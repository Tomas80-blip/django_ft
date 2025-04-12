from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Sveiki! Cia yra straipsniu sarasas.'
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'article_form.html'
    success_url = reverse_lazy('article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'article_form.html'
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
