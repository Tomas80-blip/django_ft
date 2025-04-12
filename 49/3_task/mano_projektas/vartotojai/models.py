# Užduotis: Automatinis vartotojo veiksmų
# žurnalo įrašymas
# Tikslas
# Sukurti UserLog modelį, kuris automatiškai fiksuos, kada buvo sukurtas vartotojas,
# naudodamas Django signalus.
# Užduoties aprašymas
# 1. Sukurk modelį UserLog, kuris turės šiuos laukus:
# a. user – ManyToOne ryšys su User
# b. action – Tekstas, pvz.: "Vartotojas sukurtas"
# c. timestamp – Kada įvyko veiksmas (naudoti auto_now_add=True)
# 2. Naudok post_save signalą, kad kai tik sukuriamas User, būtų sukurtas ir UserLog
# įrašas su žinute:
# "Vartotojas sukurtas"
# 3. Jei vartotojas atnaujinamas (bet ne sukuriamas), signalas neturi veikti.
# Papildoma užduotis (BONUS):
# Parašyk antrą signalą, kuris fiksuoja įrašą į UserLog, kai vartotojas yra ištrinamas (naudok
# post_delete) su tekstu:
# "Vartotojas ištrintas"


from django.db import models
from django.contrib.auth.models import User

class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    #jei useris yra pašalinamas(on_delete=models.SET_NULL) užsienio raktas bus nustatytas į NULL,
    # tai leidžia išlaikyti įrašus net jei userio nebėra sistemoje
    username=models.CharField(max_length=100)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.action} ({self.timestamp})"
