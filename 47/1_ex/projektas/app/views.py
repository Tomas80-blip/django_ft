from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q

def post_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
    else:
        posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'post_list.html',
        {
            'page_obj': page_obj,
            'query': query
        }
    )
