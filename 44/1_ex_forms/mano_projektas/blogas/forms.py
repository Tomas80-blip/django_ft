from django import forms
from .models import Post

#Pirma forma
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

#Antra forma
class KontaktuForma(forms.Form):
    vardas = forms.CharField(max_length=100)
    el_pastas = forms.EmailField()
    zinute = forms.CharField(widget=forms.Textarea)
    # Textarea padaro dideli ivesties lauka

