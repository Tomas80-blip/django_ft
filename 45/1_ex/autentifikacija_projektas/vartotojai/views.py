from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistracijosForma

def pagrindinis(request):
    return render(request, 'vartotojai/pagrindinis.html')

def registracija(request):
    if request.method == 'POST':
        form = RegistracijosForma(request.POST)
        if form.is_valid():
            form.save()
            redirect('prisijungti')
    else:
        form = RegistracijosForma()
    return render(request, 'vartotojai/registracija.html', {'form': form})

@login_required
def slaptas(request):
    return render(request, 'vartotojai/slaptas.html')
