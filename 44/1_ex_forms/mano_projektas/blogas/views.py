from django.shortcuts import render, redirect
from .forms import PostForm, KontaktuForma

def naujas_irasas(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagrindinis') #peradresuojam duomenis i bet kuri marsruta kuri mes panoresim
    else:
        form = PostForm()
    return render(request, 'naujas.html', {'form': form})
# atvaizduojam viska sablone 'naujas.html'

def kontaktai(request):
    if request.method == 'POST':
        form = KontaktuForma(request.POST)
        if form.is_valid():
            print(form.cleaned_data)# printinam i konsole kokie siuo metu duomenys
            return redirect('pagrindinis')
    else:
        form = KontaktuForma()
    return render(request, 'naujas.html', {'form': form})
# atvaizduojam viska sablone 'naujas.html'
