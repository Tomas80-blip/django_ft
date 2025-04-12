
#Sukurus nauja useri(profili automatiskai), issiunciamas el. laiskas per terminala

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # kiekvienas User objektas turi tik vieną atitinkamą Profile objektą.
    profile_picture = models.ImageField(upload_to='profiliai/', blank=True, null=True)

    def __str__(self):
        return self.user.username
