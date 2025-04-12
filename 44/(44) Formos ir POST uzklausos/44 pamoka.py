# Formos ir POST užklausos

# Tikslai
# Suprasti, kaip Django tvarko vartotojo pateikiamus duomenis per formas.
# Išmokti naudoti forms.Form ir forms.ModelForm klasėmis grįstas formas.
# Gebėti priimti ir apdoroti POST užklausas.
# Suprasti CSRF apsaugos mechanizmą.

# Teorija
# Formos Django sistemoje

# Formos Django karkase gali būti kuriamos dviem pagrindiniais būdais:
#
# forms.Form – naudojama, kai forma nėra tiesiogiai susieta su jokiu modeliu.
# forms.ModelForm – naudojama, kai forma pagrįsta konkrečiu modeliu ir leidžia greitai
# generuoti laukus pagal modelio struktūrą.

# forms.Form pavyzdys

# from django import forms
#
# class KontaktuForma(forms.Form):
#     vardas = forms.CharField(max_length=100)
#     el_pastas = forms.EmailField()
#     zinute = forms.CharField(widget=forms.Textarea)

# forms.ModelForm pavyzdys

# from django import forms
# from .models import Post
#
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'body']
# POST užklausos ir request.POST
# Kai naudotojas pateikia formą, ji siunčiama į serverį naudojant POST metodą. Django gali prieiti prie duomenų per request.POST.
#
# View funkcijoje dažniausiai patikrinama:
#
# ar užklausa yra POST
# ar forma yra užpildyta teisingai (form.is_valid())
# from django.shortcuts import render, redirect
# from .forms import PostForm
#
# def naujas_irasas(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('pagrindinis')
#     else:
#         form = PostForm()
#     return render(request, 'naujas.html', {'form': form})
# CSRF apsauga
# CSRF (Cross-Site Request Forgery) yra Django mechanizmas, apsaugantis nuo neteisėto formų pateikimo. Kiekviena forma, siunčiama POST metodu, turi turėti specialų žymeklį.
#
# Šablone reikia įdėti csrf_token:
#
# <form method="post">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Išsaugoti</button>
# </form>
# Jei šio žymens nebus, Django atmes POST užklausą kaip nesaugią.
#
# Praktika
# Sukurk forms.py faile dvi formas:
#
# Vieną paveldint iš forms.Form
# Kitą – iš forms.ModelForm, susietą su esamu modeliu Post
# Sukurk view funkciją, kuri:
#
# Tikrina, ar užklausa yra POST
# Jei forma tinkama, išsaugo duomenis ir peradresuoja naudotoją
# Jei GET, parodo tuščią formą
# Sukurk naujas.html šabloną, kuriame būtų:
#
# Forma
# csrf_token
# Mygtukas formai pateikti
# Sukurk maršrutą urls.py, kuris nukreiptų į formos puslapį.
#
# Išbandyk formos veikimą naršyklėje ir patikrink, ar įrašai išsaugomi duomenų bazėje.
#
# Sąmoningai palik laukelį tuščią ir patikrink, ar Django parodo klaidų pranešimus.
#
# Klausimai savikontrolei
# Kuo skiriasi forms.Form ir forms.ModelForm?
# Ką patikrina form.is_valid()?
# Kodėl reikia naudoti {% csrf_token %}?
# Kas nutiktų, jei POST užklausa neturėtų CSRF žymens?
# Kaip galima atvaizduoti formos klaidas šablone?
# Pages 26
# Find a page…
# Home
# Pamoka 23 SQL naudojimas Jupyter Notebook ir Db Browser SQLite
# Pamoka 24 Darbas su keliomis SQL lentelėmis
# Pamoka 25 Duomenų bazės projektavimas, constraints
# Pamoka 26 SQL Saugumas ir SQL Injection Atakos
# Pamoka 27 SQL Santykiai: One‐to‐Many ir Many‐to‐Many
# Pamoka 28
# Pamoka 29 Flask pagrindai – maršrutai, šablonai ir formos
# Pamoka 30 Flask ir SQLAlchemy – duomenų bazės valdymas
# Pamoka 31
# Pamoka 32 Kelių lentelių naudojimas Flask su SQLAlchemy
# Pamoka 33 React įvadas
# Pamoka 34 useState hook
# Pamoka 35 useEffect ir API užklausos
# Pamoka 36 React Router pagrindai
# Clone this wiki locally
# https://github.com/DariusDaskevicius/full_stack_ft_2.wiki.git
# Footer
# © 2025 GitHub, Inc.
# Footer navigation
# Terms
# Priva