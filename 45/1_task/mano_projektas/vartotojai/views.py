from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistracijosForma

def registracija(request):
    if request.method == 'POST':
        forma = RegistracijosForma(request.POST)
        if forma.is_valid():
            vartotojas = forma.save()
            login(request, vartotojas)
            return redirect('pagrindinis')
    else:
        forma = RegistracijosForma()
    return render(request, 'vartotojai/registracija.html', {'forma': forma})

def pagrindinis(request):
    return render(request, 'vartotojai/pagrindinis.html')