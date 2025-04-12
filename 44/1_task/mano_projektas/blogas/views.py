from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Vartotojas
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('Welcome to the home page!')

def register_form_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vartotojai_list')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def vartotojai_list_view(request):
    vartotojai = Vartotojas.objects.all()
    return render(request,"vartotojai_list.html",{'vartotojai': vartotojai})