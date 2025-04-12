from django.db import models
from django.contrib.auth.models import User

class Theme (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date =  models.DateField()
    organizer = models.ForeignKey(User, on_delete=models.PROTECT)
    # Vienas organizatorius gali būti susietas su keliais įrašais
    themes = models.ManyToManyField(Theme)

    def __str__(self):
        return self.title

class Registration(models.Model):
    attendee_name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    # vienas event gali turėti daug registracijų – daug prie vieno ryšys).
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Registration for {self.attendee_name }"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return f"Profile of {self.user.username}"



 # Pavyzdys: duomenų įvedimas per python manage.py shell
# # python manage.py shell
# from events.models import Event, Registration, Theme, Profile
# from django.contrib.auth.models import User
# t1 = Theme.objects.create(name='Technologijos')
# t2 = Theme.objects.create(name='Verslas')
# u = User.objects.create_user(username='Jonas', password='slaptas')
# Profile.objects.create(user=u, bio='Patyres organizatorius')
# Event.objects.create(title='startup renginys', description='Apie inovacijas', date='2023-03-31', organizer=u)



