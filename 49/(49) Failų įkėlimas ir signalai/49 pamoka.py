
# Terminale
# pip install pillow

# Tema: Failų įkėlimas ir signalai
# Tikslai
# Išmokti įkelti ir rodyti paveikslėlius ar kitus failus naudojant Django modelius ir formas.
# Suprasti, kaip naudoti signalus tam tikrų veiksmų automatizavimui.
# Suprasti, kada naudoti signalus, o kada logiką rašyti tiesiogiai vaizduose arba modeliuose.
# Teorija
# MEDIA_URL ir MEDIA_ROOT
# Django projekte failų įkėlimui būtina aiškiai nurodyti, kur bus saugomi įkelti failai (serveryje) ir kokiu adresu jie bus pasiekiami naršyklėje.
#
# MEDIA_ROOT – tai serverio kelias į katalogą, kuriame laikomi įkelti failai.
# MEDIA_URL – tai URL prefiksas, per kurį šie failai bus pasiekiami naršyklėje.
# Šie nustatymai rašomi settings.py faile:
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Tam, kad failai veiktų vystymo (development) metu, urls.py faile turi būti įtraukti šie nustatymai:
#
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#     # kiti maršrutai
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Šis sprendimas tinka tik vystymo aplinkoje. Produkcijoje statiniais failais turėtų rūpintis specialus serveris (pvz. NGINX).
#
# ImageField ir FileField
# Django modeliuose naudojame šiuos laukus failų įkėlimui:
#
# FileField – leidžia įkelti bet kokį failą (PDF, DOCX, ZIP ir kt.).
# ImageField – leidžia įkelti tik paveikslėlius. Reikalinga biblioteka Pillow, kuri leidžia apdoroti vaizdus Python'e.
# Diegimas:
#
# pip install pillow
# Pavyzdys – modelis su profilio nuotrauka:
#
# from django.db import models
# from django.contrib.auth.models import User
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='profiliai/', blank=True, null=True)
# Argumentas upload_to='profiliai/' nurodo, kad failai bus įrašyti į media/profiliai/ aplanką.
#
# Failų atvaizdavimas šablone
# Norint parodyti įkeltą paveikslėlį šablone, būtina naudoti .url:
#
# <img src="{{ user.profile.profile_picture.url }}" alt="Profilio nuotrauka">
# Taip pat įsitikink, kad šablone yra įkelta statinių failų sistema:
#
# {% load static %}
# Failai bus pasiekiami tik tuo atveju, jei naršyklė galės juos nuskaityti per MEDIA_URL.
#
# Signalai
# Signalai yra Django mechanizmas, kuris leidžia reaguoti į įvykius duomenų bazėje, tokius kaip objekto sukūrimas, atnaujinimas ar ištrynimas.
#
# Pagrindiniai signalų tipai:
#
# pre_save – prieš įrašant duomenis į DB
# post_save – po įrašo sukūrimo arba atnaujinimo
# pre_delete – prieš objektą ištrinant
# post_delete – po objekto ištrynimo
# Signalai leidžia išskaidyti logiką ir užtikrinti, kad tam tikri veiksmai visada įvyks, nepriklausomai nuo to, kaip duomenys buvo sukurti (admin, view, shell ar API).
#
# Pavyzdys: automatinis Profile sukūrimas
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile
#
# @receiver(post_save, sender=User)
# def sukurti_profili(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# Tai reiškia: kai tik sukuriamas naujas User objektas, automatiškai bus sukurtas ir jam priskirtas Profile objektas.
#
# Signalų aktyvavimas
# Kad signalai veiktų, jie turi būti importuoti. Įprasta praktika:
#
# Sukurti failą signals.py aplikacijoje.
# Importuoti jį apps.py faile, perrašius ready() metodą:
# class BlogasConfig(AppConfig):
#     name = 'blogas'
#
#     def ready(self):
#         import blogas.signals
# Be šio importavimo signalai nebus aktyvuoti.
#
# Kada naudoti signalus, o kada ne?
# Signalus naudoti verta, kai:
#
# Reikia užtikrinti, kad kažkas visada įvyktų sukūrus / atnaujinus / ištrynus objektą.
# Veiksmas turi būti automatinis (nepriklausomas nuo to, iš kur objektas sukurtas).
# Geriau nenaudoti signalų, kai:
#
# Logika yra specifinė konkrečiam view arba formos pateikimui.
# Reikia grįžtamojo ryšio vartotojui (pvz. pranešimo apie rezultatą).
# Praktika
# Pridėk ImageField prie modelio Profile su upload_to='profiliai/'.
# Sukurk ModelForm, kuris leidžia redaguoti profile_picture lauką.
# views.py faile:
# if request.method == 'POST':
#     form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#     if form.is_valid():
#         form.save()
# Šablone parodyk įkeltą paveikslėlį su {{ user.profile.profile_picture.url }}.
# Įsitikink, kad veikia failų rodymas per MEDIA_URL.
# Sukurk signals.py ir post_save signalą, kuris automatiškai sukuria Profile objektą naujam User.
# Sukurk kitą signalą, kuris:
# ištrina paveikslėlį, jei ištrinamas profilis (naudok post_delete), arba
# išsiunčia el. laišką įvykus veiksmui.
# Klausimai savikontrolei
# Kam naudojamas MEDIA_ROOT ir MEDIA_URL? Ką jie daro?
# Kodėl būtina naudoti request.FILES, kai forma turi failą?
# Kuo skiriasi FileField ir ImageField? Kada naudoti kurį?
# Kodėl signalai naudingi didesniuose projektuose?
# Kaip importuoti signals.py, kad jis veiktų tinkamai?
# Kaip veikia post_save signalas ir kaip patikrinti, ar objektas naujas (created=True)?