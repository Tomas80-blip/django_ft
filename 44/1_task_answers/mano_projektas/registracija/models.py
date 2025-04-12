from django.db import models

class Registracija(models.Model):
    vardas = models.CharField(max_length=100)
    el_pastas = models.EmailField(unique=True)
    sukurta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vardas} ({self.el_pastas})'
