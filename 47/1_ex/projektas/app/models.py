from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


# per shell'a prideti 200 postu po kodo parasymo

# python manage.py shell

# >> > from app.models import Post
# >> > for i in range(1, 201):
#         Post.objects.create(title=f'Postas Nr. {i}', body=f'Tai yra posto body Nr. {i}')
# exit
# ir python manage.py runserver