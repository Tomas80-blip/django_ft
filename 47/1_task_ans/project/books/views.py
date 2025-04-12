from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
from django.db.models import Q


def book_list(request):
    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'book_list.html',
        {
            'page_obj': page_obj,
            'query': query,
        }
    )

