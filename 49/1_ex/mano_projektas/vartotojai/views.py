from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm

@login_required
def redaguoti_profili(request):
    profilis = request.user.profile
# jei redaguojam forma tai viska issaugom ir griztam i 'profilis'
    if request.method == 'POST':
        forma = ProfileForm(request.POST, request.FILES, instance=profilis)
        if forma.is_valid():
            forma.save()
            return redirect('profilis')
    else:
    # su GET tiesiog gaunam profili
        forma = ProfileForm(instance=profilis)
    return render(request, 'profilis.html', {'forma': forma})
