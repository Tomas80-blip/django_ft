from django.db import models

class Feedback(models.Model):
    vardas = models.CharField(max_length=100)
    el_pastas = models.EmailField()
    zinute = models.TextField()
    sukurta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vardas} ({self.el_pastas})'
