from django.shortcuts import render, redirect
from .forms import RegistracijosForma
from .models import Registracija

def registracija_view(request):
    if request.method != 'POST':
        form = RegistracijosForma()
    else:
        form = RegistracijosForma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dalyviai')
    return render(request, 'registracija.html', {'form': form})

def dalyviai_view(request):
    visi = Registracija.objects.all().order_by('-sukurta')
    return render(request, 'dalyviai.html', {'dalyviai': visi})
