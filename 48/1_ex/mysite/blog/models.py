from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()

 # python manage.py shell

# from blog.models import Post
# for i in range(1, 201):
#    ...:      Post.objects.create(title=f'Title {i}', author=f'Author {i}')


