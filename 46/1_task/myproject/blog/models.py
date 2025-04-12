# Užduotis: Sukurk paprastą renginių registracijos sistemą su naudotojų profiliais, renginiais,
# registracijomis ir temomis
# Modelių kūrimas
# Sukurk šiuos modelius models.py faile:
# 1.1 Theme modelis:
# Laukas name (CharField)
# Bus naudojamas ManyToMany ryšiui
# 1.2 Event modelis:
# title, description laukai
# themes – ManyToManyField į Theme
# organizer – ForeignKey į User (naudok on_delete=PROTECT, kad negalima būtų
# ištrinti organizatoriaus su renginiais)
# 1.3 Registration modelis:
# comment
# event – ForeignKey į Event, su on_delete=CASCADE
# related_name='registrations'
# 1.4 Profile modelis:
# bio
# user – OneToOneField į User, on_delete=CASCADE
# Admin registracija (admin.py)
# Užregistruok visus modelius admin panelėje: Theme, Event, Registration, Profile
# Migracijos
# Vykdyk komandų seką:
# python manage.py makemigrations python manage.py migrate
# Testavimas per Django shell
# Vykdyk:
# python manage.py shell
# Atlik šiuos veiksmus per shell:
# Sukurk kelias temas
# Sukurk naudotoją (naudok User.objects.create_user(...))
# Sukurk Profile šiam naudotojui
# Sukurk Event naudodamas šį naudotoją kaip organizatorių
# Pridėk temas prie renginio su .themes.add(...)
# Sukurk kelias registracijas tam renginiui
# Ištrink Event – patikrink, ar registracijos buvo ištrintos (CASCADE)
# Bandyk ištrinti naudotoją – turėtum gauti klaidą dėl PROTECT
# Sukurk šabloną event_detail.html
# Jis turėtų:
# Rodyti renginio title ir description
# Išvesti visų jo temų pavadinimus
# Išvesti visų susijusių registracijų komentarus


from django.db import models
from django.contrib.auth.models import User

class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    themes = models.ManyToManyField(Theme)
    organizer = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Registration for {self.event.title}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return f"Profile of {self.user.username}"


# Testavimas per python manage.py shell
# from django.contrib.auth.models import User
# from blog.models import Theme, Event, Registration, Profile
# t1 = Theme.objects.create(name="Technologijos")
# user = User.objects.create_user(username='jonas', password='slaptazodis'
# profile = Profile.objects.create(user=user, bio="Labas! Aš esu Jonas.")
# event = Event.objects.create(title="AI Konferencija", description="Apie dirbtinį intelektą", organizer=user)
# reg1 = Registration.objects.create(comment="Laukiu renginio!", event=event)
# reg2 = Registration.objects.create(comment="Bus įdomu!", event=event)
# event.registrations.all()
# event.delete()
# Registration.objects.all()  # Turėtų būti tuščia

# Bandymas ištrinti naudotoją – turėtų gauti klaidą dėl PROTECT
# user.delete()
# exit

