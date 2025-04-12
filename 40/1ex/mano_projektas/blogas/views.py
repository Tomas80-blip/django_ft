from django.shortcuts import render

from django.http import HttpResponse

def pagrindinis(request):
    kontekstas = {
        'pavadinimas': 'Mano Puslapis',
        'antraste': 'Sveiki atvyke i pagrindini puslapi'
    }
    # kontekstas bus perduodamas i pagrindinis.html
    return render(request, 'pagrindinis.html', kontekstas)
# pagrindinis veikia su django templates

def apie(request):
    return HttpResponse('Cia yra apie puslapis')
# cia ne pagrindinis ir jei reikia pasiimti duomenis i React ar Flask