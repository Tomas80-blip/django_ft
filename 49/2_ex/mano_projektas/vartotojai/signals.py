from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Profile
import os

@receiver(post_save, sender=User)
def sukurti_profili(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Kai Profile objektas yra ištrinamas tai automatiškai ištrinama profilio nuotrauką iš serverio
# (t.y. istrinama is media/profiliai)
@receiver(post_delete, sender=Profile)
def istrinti_paveiksleli(sender, instance, **kwargs):
    if instance.profile_picture and os.path.isfile(instance.profile_picture.path):
# Patikrinama, ar egzistuoja profilio nuotrauka ir ar failas tikrai egzistuoja serveryje
        os.remove(instance.profile_picture.path)
# ištrina (pašalina) failą iš serverio, naudodama jo kelią (path).
