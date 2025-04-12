# Modeliai ir duomenų bazės valdymas su Django

# Tikslai
# Suprasti, kaip Django modeliai leidžia kurti duomenų struktūrą panaudojant Python kalbą.
# Išmokti sukurti modelius ir juos registruoti aplikacijoje.
# Suprasti, kaip Django generuoja ir naudoja migracijas.
# Naudotis manage.py shell testuojant modelių funkcionalumą.

# Teorija
# Django modelių sistema
# Django modeliai yra centrinė vieta, kurioje aprašoma, kaip duomenys saugomi. Modelis yra Python klasė,
# paveldinti iš django.db.models.Model.
# Django automatiškai konvertuoja modelius į SQL lenteles pagal nurodytas savybes (laukelius).
#
# Modelio apibrėžimas:
#
# from django.db import models
#
# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
# CharField naudojamas trumpiems tekstams (būtinas max_length).
# TextField leidžia rašyti ilgus tekstus.
# DateTimeField su auto_now_add=True reiškia, kad reikšmė bus automatiškai užpildyta objekto sukūrimo metu.

# Django taip pat automatiškai prideda kiekvienam modeliui id lauką (pirminį raktą).
#


# Modelių registravimas admin panelėje

# Kad būtų galima tvarkyti duomenis per administravimo sąsają, modelį reikia registruoti admin.py faile:
#
# from django.contrib import admin
# from .models import Post
#
# admin.site.register(Post)

# Tada, prisijungus prie http://127.0.0.1:8000/admin, matysi lentelę „Posts“,
# jei esi sukūręs supervartotoją:
#
# python manage.py createsuperuser

# Migracijos: modelių pavertimas SQL lentelėmis

# Kai sukuri ar pakeiti modelį, reikia atnaujinti duomenų bazę. Tam naudojamos migracijos:
#
# python manage.py makemigrations – sugeneruoja migracijos failą, aprašantį modelio pokyčius.
# python manage.py migrate – įrašo pokyčius į faktinę duomenų bazę (sukuria ar keičia lenteles).

# Migracijos leidžia palaikyti tvarkingą, versijuojamą duomenų struktūros evoliuciją.
#


# Django ir SQLite
# Pagal nutylėjimą Django projektas naudoja SQLite duomenų bazę. Tai yra paprasta, bet funkcionali failinė DB, kuri idealiai tinka mokymuisi ir prototipų kūrimui.
#
# db.sqlite3 – failas, kuriame saugomi visi duomenys.
#
# Jeigu planuojama naudoti PostgreSQL ar kitą DB sistemą, tai vėliau galima nurodyti settings.py faile:
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mano_duombaze',
#         'USER': 'vartotojas',
#         'PASSWORD': 'slaptazodis',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# Praktika

# Sukurk modelį Post su šiais laukais:
#
# title: CharField (iki 200 simbolių)
# body: TextField
# created_at: DateTimeField su auto_now_add=True
# Įrašyk šį modelį į models.py savo aplikacijoje.
#
# Paleisk migracijas:
#
# python manage.py makemigrations
# python manage.py migrate

# Užregistruok modelį admin.py faile, kad jį būtų galima redaguoti per admin sąsają.
#
# Sukurk supervartotoją:
#
# python manage.py createsuperuser

# Prisijunk prie admin panelės adresu http://127.0.0.1:8000/admin ir
# sukurk naują Post įrašą per sąsają.
#
# Naudodamasis python manage.py shell, atlik šiuos veiksmus:
#
# from blogas.models import Post
# Post.objects.create(title="Pirmas įrašas", body="Tai yra turinys")
# Post.objects.all()

# Klausimai savikontrolei
# Kodėl migracijos yra būtinos kuriant ar keičiant modelius?
# Kokiais atvejais naudojamas auto_now_add=True ir kuo jis skiriasi nuo auto_now=True?
# Kur laikomi migracijų failai ir kokį vaidmenį jie atlieka?
# Kodėl verta naudoti admin sąsają testuojant modelių veikimą?
# Ar galima pakeisti modelio pavadinimą nekeičiant duomenų bazės struktūros? Kodėl taip arba ne?
