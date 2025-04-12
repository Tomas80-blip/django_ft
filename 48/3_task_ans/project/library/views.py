from django.views.generic import ListView, DetailView, CreateView
from .models import Book
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')
