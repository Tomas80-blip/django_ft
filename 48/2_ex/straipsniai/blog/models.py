from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


 # python manage.py shell

# from blog.models import Article
# for i in range(1, 201):
#    ...:      Article.objects.create(title=f'Title {i}', content=f'Kontentas {i}')