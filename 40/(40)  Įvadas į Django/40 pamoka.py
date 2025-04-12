# ĮVADAS Į DJANGO IR PIRMA PAMOKA

# Tikslai:
# Suprasti, kas yra Django, kam jis skirtas ir kuo skiriasi nuo kitų sistemų.
# Įsidiegti Django į savo kompiuterį.
# Sukurti naują Django projektą ir aplikaciją.
# Suprasti projekto ir aplikacijos struktūrą.
# Paleisti serverį ir matyti pirmą rezultatą naršyklėje.

# Teorija
# Kas yra Django?
# Django – tai "framework’as" (programų karkasas), skirtas kurti žiniatinklio (web)
# aplikacijas naudojant Python programavimo kalbą.
#
# Jis padeda kurti svetaines greitai ir saugiai, nes turi labai daug įrankių „iš dėžutės“:
#
# Admin panelė
# Prisijungimas / registracija
# Darbas su duomenų baze (ORM)
# Apsauga nuo SQL injekcijų ir CSRF atakų
# Šablonų (templates) sistema

# Kodėl naudoti Django?
# Privalumai	                            Paaiškinimas
# „Bateries included“	           Daug funkcijų jau yra (nereikia kurti nuo nulio)
# Saugumas	                       Automatinė apsauga nuo daugelio atakų
# Admin panelė	                   Galingas įrankis duomenų valdymui
# Didelė bendruomenė	           Daug dokumentacijos, bibliotekų ir pamokų
# Greita plėtra	                   Aiški struktūra padeda greitai auginti projektą

# Django struktūra: MTV
# Django remiasi MTV (Model - Template - View) struktūra:
# Model – objektai, atspindintys duomenų bazės lenteles.
#
# Template – HTML su specialiais Django žymėjimais (šablonai).
#
# View – Python funkcijos ar klasės, kurios apdoroja užklausas ir pateikia atsakymus.
#
# Django „View“ ≈ MVC „Controller“, o „Template“ ≈ MVC „View“
#

# Praktika
# Django diegimas
#
# python -m venv venv
# source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate     # Windows
# pip install django
# python -m django --version


# Naujo projekto kūrimas
#
# django-admin startproject mano_projektas
# cd mano_projektas


# Struktūra:
#
# mano_projektas/
# ├── manage.py                # Projekto valdymo įrankis
# └── mano_projektas/
#     ├── __init__.py
#     ├── settings.py          # Nustatymai
#     ├── urls.py              # Maršrutai
#     ├── asgi.py              # ASGI serverio įėjimas
#     └── wsgi.py              # WSGI serverio įėjimas

# Ką darome rašydami:
#
# django-admin startproject mano_projektas

# Ką ši komanda daro?#
# Sukuria Django projekto struktūrą.

# Kodėl tai reikia daryti?#
# Be projekto neturėsime settings.py, urls.py, manage.py ir kitų svarbių failų.

# Rezultatas:#
# Turime pagrindinį karkasą, nuo kurio prasidės visa svetainė

# Aplikacijos (app) kūrimas#
# python manage.py startapp blogas

# Struktūra:
#
# blogas/
# ├── admin.py          # Admin panelės valdymas
# ├── apps.py           # Konfigūracija
# ├── models.py         # Duomenų modeliai
# ├── views.py          # Vaizdai (logika)
# ├── tests.py          # Testai
# └── migrations/       # Migracijos (DB pokyčiai)

# Ką darome rašydami:#
# python manage.py startapp blogas

# Ką ši komanda daro?#
# Sukuria naują Django aplikaciją (funkcinį modulį).

# Kodėl tai reikia daryti?#
# Aplikacijos yra vietos, kur rašome visą logiką: modelius, vaizdus, šablonus.

# Rezultatas:
# Turime atskirą komponentą, kurį galime naudoti net ir kituose projektuose.

# Nepamiršk: aplikaciją reikia pridėti į settings.py:
#
# INSTALLED_APPS = [
#     ...
#     'blogas',
# ]


# Serverio paleidimas#
# python manage.py runserver

# Naršyklėje atsidaryk:
# http://127.0.0.1:8000

# Jei viskas gerai – matysi Django sveikinimo puslapį!