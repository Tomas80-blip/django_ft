from django import forms
from .models import Vartotojas

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Vartotojas
        fields = ['vardas', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Vartotojas.objects.filter(email=email).exists():
            raise forms.ValidationError('Sis el.pastas jau uzregistruotas.')
        return email
