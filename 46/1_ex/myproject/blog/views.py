from django.shortcuts import render, get_object_or_404
from .models import Post

#leidzia matyti posta pagal id
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})
