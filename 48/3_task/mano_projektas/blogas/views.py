
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Book


class BookListView(ListView):
    model = Book
    tamplate_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    tamplate_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author']
    auccess_url = reverse_lazy('book_list')