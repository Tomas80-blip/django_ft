# 1. URL maršrutai
# Užduotis: Sukurkite naują maršrutą, kuris atitinka adresą /kontaktai/ ir atvaizduoja
# tekstą „Susisiekite su mumis!“.
# Instrukcija:
# 1. Atidarykite blogas/urls.py.
# 2. Pridėkite naują path('kontaktai/', views.kontaktai,
# name='kontaktai').
# 3. Sukurkite atitinkamą kontaktai() funkciją views.py faile.
# 4. Naudokite HttpResponse().
# 2. View funkcijos
# Užduotis: Sukurkite naują view funkciją naujienos, kuri perduoda šiuos duomenis į
# šabloną:
# • 'pavadinimas': 'Naujienos'
# • 'antraste': 'Šviežiausios naujienos'
# Instrukcija:
# 1. Sukurkite naujienos() funkciją views.py faile.
# 2. Sukurkite šabloną naujienos.html.
# 3. Įtraukite naują maršrutą path('naujienos/', views.naujienos) į urls.py.
# 3. Šablonų struktūra
# Užduotis: Sukurkite naują HTML šabloną apie.html, kuris:
# • Rodo puslapio pavadinimą viršuje (<title>).
# • Rodo antraštę (<h1>).
# • Prideda paragrafą su tekstu „Šis puslapis skirtas informacijai apie mus.“
# Instrukcija:
# 1. Sukurkite failą blogas/templates/apie.html.
# 2. Perkelkite apie() funkciją į render() vietoj HttpResponse().
# 3. Į views.py pridėkite kontekstas su pavadinimas ir antraste.
# 4. render() ir context perdavimas
# Užduotis: Sukurkite naują puslapį /autorius/, kuris HTML šablone rodytų autoriaus
# vardą ir pomėgius.
# Instrukcija:
# 1. views.py sukurkite autorius() funkciją.
# 2. Naudokite render() ir perduokite kintamuosius:
# a. 'vardas': 'Jonas'
# b. 'pomegiai': ['Programavimas', 'Dviračiai', 'Kava']
# 3. Sukurkite autorius.html šabloną su {{ vardas }} ir for ciklu parodykite
# pomėgių sąrašą.

from django.shortcuts import render
from django.http import HttpResponse

def pagrindinis(request):
    kontekstas = {
        'pavadinimas': 'Mano Puslapis',
        'antraste': 'Sveiki atvyke i pagrindini puslapi!'
    }
    return render(request, 'pagrindinis.html', kontekstas)


def kontaktai(request):
    return HttpResponse('Susisiekite su mumis!')

def naujienos(request):
    kontekstas = {
        'pavadinimas': 'Naujienos',
        'antraste': 'Svieziausios naujienos'
    }
     # kontekstas bus perduodamas i pagrindinis.html
    return render(request, 'naujienos.html', kontekstas)

def apie(request):
    context = {
        'pavadinimas': 'Apie mus',
        'antraste': 'Kas mes esame?'
    }
    return render(request, 'apie.html', context)

def autorius(request):
    context = {
        'vardas': 'Jonas',
        'pomegiai': ['Programavimas', 'Dviraciai', 'Kava']
    }
    return render(request, 'autorius.html', context)
