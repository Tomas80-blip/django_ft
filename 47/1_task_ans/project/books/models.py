from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

# def create_books():
#     for i in range(1, 201):
#         Book.objects.create(
#             title=f'Knyga Nr. {i}',
#             author=f'Autorius {"A" if i % 2 == 0 else "B"}',
#             description=f'Tai yra aprasymas apie knyga numeris {i}',
#         )


# 1 variantas pakisti funkcija def create_books(): po class Book(models.Model):
# 2 variantas
# paleidziam sheel
# python manage.py shell
# from books.models import Book
# from books.models import create_books
# create_books()
# exit

# po shell funkcija def create_books(): uzkomentuojam kai sukuriam modelius
# python manage.py runserver