from django.shortcuts import render
from .forms import NuotraukaForm

def ikelti_nuotrauka(request):
    paveikslelis = None
    if request.method == 'POST':
        form = NuotraukaForm(request.POST, request.FILES)
        if form.is_valid():
            paveikslelis = form.save()
    else:
        form = NuotraukaForm()
    return render(request, 'ikelti.html', {'form': form, 'paveikslelis': paveikslelis})
