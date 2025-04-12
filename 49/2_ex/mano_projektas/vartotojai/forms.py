from django import forms
from .models import Profile


# nuotraukų įkėlimo formą
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
