from django import forms
from .models import Registracija

class RegistracijosForma(forms.ModelForm):
    class Meta:
        model = Registracija
        fields = ['vardas', 'el_pastas']

    def clean_el_pastas(self):
        el_pastas = self.cleaned_data['el_pastas']
        el_pastas_exists = Registracija.objects.filter(el_pastas=el_pastas).exists()
        if el_pastas_exists:
            raise forms.ValidationError('Sis el. pastas jau uzregistruotas.')
        return el_pastas
