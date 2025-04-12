from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profilis

#VartotojoRegistracijosForm paveldi UserCreationForm – tai Django standartinė forma, naudojama registracijai.
class VartotojoRegistracijosForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    #Pridedamas papildomas laukelis full_name, kuris neįeina į User modelį, todėl jis apdorojamas atskirai.

    class Meta:
        #Meta klasėje nustatoma, kad forma veikia su User modeliu ir leidžia įvesti tik tam tikrus
        # laukus (username, email, password1, password2).
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super().save(commit) #pirmiausia kviečiamas UserCreationForm metodas save(), kuris
        # išsaugo naują User modelio objektą. Išsaugo vartotoją naudojant tėvinės klasės metodą
        Profilis.objects.create(user=user, full_name=self.cleaned_data['full_name'])
        #Sukuriamas Profilis objektas:
        # Profilis.objects.create(...) sukuria naują Profilis modelio įrašą, kuris:
        # user=user – susiejamas su naujai sukurtu vartotoju.        #
        # full_name=self.cleaned_data['full_name'] – įrašo pilną vardą, kurį įvedė vartotojas formoje.
        return user
