# Užduoties reikalavimai:
# 1. Sukurkite Django aplikaciją pavadinimu katalogas, jeigu jos dar neturite.
# 2. Sukurkite modelius Author ir Book:
# a. Author turi laukus: vardas ir pavardė (iki 100 simbolių), gimimo metai.
# b. Book turi laukus: pavadinimas (iki 200 simbolių), ryšys su autoriumi
# (ForeignKey), ir išleidimo data.
# 3. Paleiskite migracijas, kad modeliai būtų sukurti duomenų bazėje.
# 4. Registruokite modelius admin.py faile. BookAdmin klasėje nurodykite
# list_display su stulpeliais: pavadinimas, autorius, data. Taip pat pridėkite
# filtravimą pagal autorių ir datą.
# 5. Sukurkite supervartotoją ir prisijunkite prie admin panelės adresu
# http://127.0.0.1:8000/admin.
# 6. Per admin sąsają:
# a. Sukurkite bent 2 autorius.
# b. Kiekvienam pridėkite bent po 2 knygas.
# 7. Naudodami python manage.py shell, atlikite šiuos veiksmus:
# a. Sukurkite naują Author objektą.
# b. Sukurkite bent vieną Book objektą, susietą su šiuo autoriumi.
# c. Išveskite visas konkretaus autoriaus knygas.


# Darbas per sell’a
# python manage.py shell
# from katalogas.models import Author, Book
# # a1 = Author.objects.create(vardas='Antanas', pavarde = 'Skema', gimimo_metai=1980)
# Book.objects.create(pavadinimas='Balta drobule', autorius=a1, isleidimo_data='1958-01-01')
# <Book: Balta drobule>
# a1.book_set.all()
# <QuerySet [<Book: Balta drobule>]>
# exit()



from django.db import models

class Author(models.Model):
    vardas = models.CharField(max_length=100)
    pavarde = models.CharField(max_length=100)
    gimimo_metai = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vardas} {self.pavarde}'

class Book(models.Model):
    pavadinimas = models.CharField(max_length=200)
    autorius = models.ForeignKey(Author, on_delete=models.CASCADE)
    isleidimo_data = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pavadinimas}'

    class Meta:
        ordering = ['-created_at']

