from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserLog

@receiver(post_save, sender=User)
def registruoti_sukurima(sender, instance, created, **kwargs):
    if created:
        UserLog.objects.create(
            user=instance,
            username=instance.username,
            action='Vartotojas sukurtas'
        )

@receiver(post_delete, sender=User)
def registruoti_istrynima(sender, instance, **kwargs):
    UserLog.objects.create(
        username=instance.username,
        action='Vartotojas istrintas'
    )
