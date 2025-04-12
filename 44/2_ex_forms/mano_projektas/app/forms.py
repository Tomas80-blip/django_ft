from traceback import format_exc

from django import forms
from .models import Feedback

#Pirma forma
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['vardas', 'el_pastas', 'zinute']

    def clean_zinute(self):
        zinute = self.cleaned_data['zinute']
        if 'keiksmazodis' in zinute.lower():
            raise forms.ValidationError('Zinuteje yra netinkamu zodziu.')
        return zinute

#Antra forma
class GreitaZinuteForma(forms.Form):
    el_pastas = forms.EmailField()
    zinute = forms.CharField(widget=forms.Textarea)
    #Textarea padaro dideli ivesties lauka