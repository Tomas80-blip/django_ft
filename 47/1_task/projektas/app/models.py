# Užduotis: Knygų katalogas su paieška ir puslapiavimu
# Užduoties tikslas:
# Sukurti paprastą knygų sąrašo puslapį, kuriame naudotojas galėtų:
# • Peržiūrėti visas knygas, 5 viename puslapyje
# • Ieškoti knygų pagal pavadinimą arba autorių
# • Naršyti tarp rezultatų puslapių
# Reikalavimai:
# 1. Modelis Book
# Turi šiuos laukus:
# a. title (CharField)
# b. author (CharField)
# c. description (TextField)
# 2. View funkcija
# a. Naudoja Paginator, kad rodytų po 5 knygas viename puslapyje
# b. Leidžia ieškoti knygų pagal title arba author (naudojant Q objektą)
# c. Paieškai naudoti GET formą su lauku q
# 3. Šablonas
# a. Rodo paieškos laukelį
# b. Atvaizduoja knygas iš page_obj
# c. Turi mygtukus „Ankstesnis“ / „Kitas“, kurie išlaiko paieškos parametrą
# Pavyzdinis scenarijus:
# 1. Atidarai puslapį /knygos/
# 2. Matai 5 knygas ir mygtuką „Kitas“
# 3. Į paiešką įvedi „Orwell“ – matai tik knygas, kurių autorius arba pavadinimas susijęs
# su Orwell
# 4. Spaudi „Kitas“ – paieška vis dar galioja, matai antrą rezultatų puslapį

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.author}"


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
# from app.models import Book
# from app.models import create_books
# create_books()
# exit

# po shell funkcija def create_books(): uzkomentuojam kai sukuriam modelius
# python manage.py runserver
