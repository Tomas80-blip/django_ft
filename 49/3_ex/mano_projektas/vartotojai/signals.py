from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def sukurti_profili_ir_siusti_laiska(sender, instance, created, **kwargs):
    email = 'aaa@gmail.com'

    # sukuriamas profilis kartu su useriu kaip instancija
    Profile.objects.create(user=instance)

    # jei useris turi email'a
    if email:
        send_mail(
            subject='Sveiki prisijunge!',
            message='Jusu profilis sukurtas sekmingai.',
            from_email=None, #naudos default emaila is settings.py
            recipient_list=[email],
            fail_silently=True
        )
    if not created:
        return
