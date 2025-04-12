from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiliai/', blank=True, null=True)
# upload_to = 'profiliai/'  nurodo, kad nuotraukos bus saugomos kataloge media/profiliai/ tavo Django projekte.
    def __str__(self):
        return self.user.username
