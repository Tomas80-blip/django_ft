from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VartotojoRegistracijosForm
from .models import Profilis

def registracija(request):
    if request.method == 'POST':
        form = VartotojoRegistracijosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prisijungti')
    else:
        form = VartotojoRegistracijosForm()
    return render(request, 'vartotojai/registracija.html', {'form': form})

@login_required
def profilis(request):
    return render(request, 'vartotojai/profilis.html', {'profilis': request.user.profilis})

@login_required
def redaguoti_profili(request):
    profilis = request.user.profilis
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        profilis.full_name = full_name
        profilis.save()
        return redirect('profilis')
    return render(request, 'vartotojai/redaguoti_profili.html', {'profilis': profilis})

@login_required
def naudotoju_sarasas(request):
    if not request.user.is_staff:
        return redirect('profilis')
    visi = Profilis.objects.all()
    print(visi)
    return render(request, 'vartotojai/naudotoju_sarasas.html', {'vartotojai': visi})
