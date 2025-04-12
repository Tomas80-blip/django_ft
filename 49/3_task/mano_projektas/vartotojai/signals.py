from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserLog

@receiver(post_save, sender=User)
def log_user_creation(sender, instance, created, **kwargs):
    if not created:
        return
    UserLog.objects.create(user=instance, username=instance.username, action="Vartotojas sukurtas")

@receiver(post_delete, sender=User)
def log_user_deletion(sender, instance, **kwargs):
    UserLog.objects.create(username=instance.username, action="Vartotojas ištrintas")
