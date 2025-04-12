from django.shortcuts import render
from django.http import HttpResponse

def pagrindinis(request):
    kontekstas = {
        'pavadinimas': 'Mano Puslapis',
        'antraste': 'Sveiki atvyke i pagrindini puslapi'
    }
    return render(request, 'pagrindinis.html', kontekstas)

def apie(request):
    context = {
        'pavadinimas': 'Apie mus',
        'antraste': 'Kas mes esame?'
    }
    return render(request, 'apie.html', context)

def kontaktai(request):
    return HttpResponse(
        '''
        
        <a href="google.com">Super link</a>
        <ul>
            <li>123</li>
            <li>123</li>
            <li>123</li>
        </ul>
        '''
        # siuos metodu geriau naudoti html'e
    )

def naujienos(request):
    context = {
        'pavadinimas': 'Naujienos',
        'antraste': 'Svieziausios naujienos'
    }
    return render(request, 'naujienos.html', context)

def autorius(request):
    context = {
        'vardas': 'Jonas',
        'pomegiai': ['Programavimas', 'Dviraciai', 'Kava']
    }
    return render(request, 'autorius.html', context)
