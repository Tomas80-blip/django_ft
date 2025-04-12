# Vieno paveikslėlio įkėlimas ir
# atvaizdavimas
# �
# � Užduoties tikslas
# Sukurti Django aplikaciją, kuri leidžia įkelti paveikslėlį ir jį peržiūrėti po įkėlimo.
# Užduoties sąlyga
# 1. Modelis: Sukurkite modelį Nuotrauka su vienu lauku:
# a. paveikslelis: ImageField su upload_to='nuotraukos/'
# 2. Forma: Sukurkite ModelForm, kuri leidžia įkelti paveikslėlį.
# 3. View: Sukurkite view funkciją ikelti_nuotrauka, kuri:
# a. Rodo formą GET metodu.
# b. Įkelia paveikslėlį ir parodo jį POST metodu.
# 4. Šablonas: Sukurkite HTML formą su failo įkėlimo lauku ir mygtuku „Įkelti“.
# a. Po įkėlimo parodykite įkeltą paveikslėlį.
# 5. Failų rodymas:
# a. Sutvarkykite settings.py, kad veiktų MEDIA_ROOT ir MEDIA_URL.
# b. urls.py turi leisti rodyti įkeltus failus.
# Failai, kuriuos reikia redaguoti
# • models.py
# • forms.py
# • views.py
# • urls.py (projekto ir aplikacijos)
# • templates/nr/ikelti.html
# • settings.py (tik MEDIA nustatymai)
# Pavyzdys, ką galutinis vartotojas mato
# 1. Forma su „Pasirinkti failą“ ir mygtuku „Įkelti“.
# 2. Po įkėlimo – formos apačioje rodomas paveikslėlis.


from django.db import models


#issaugom aplankale media/nuotraukos
class Nuotrauka(models.Model):
    paveikslelis = models.ImageField(upload_to='nuotraukos/')

    def __str__(self):
        return f'Nuotrauka {self.id}'
