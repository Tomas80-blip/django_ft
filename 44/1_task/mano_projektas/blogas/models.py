# Užduotis: Registracijos į renginį forma
# Tikslas: Sukurti registracijos sistemą, kurioje vartotojas gali užsiregistruoti į renginį
# pateikdamas savo vardą ir el. paštą. Sistema turi apdoroti POST užklausas, naudoti Django
# formas, atlikti duomenų validaciją ir apsaugoti formą nuo pasikartojančių registracijų.
# Reikalavimai:
# Modelis Sukurkite modelį, kuris saugotų šiuos laukus:
# • Vardas (tekstas)
# • El. paštas (turi būti unikalus – su tuo pačiu el. paštu galima registruotis tik vieną
# kartą)
# • Registracijos data/laikas (automatiškai nustatomas)
# Forma
# • Naudokite ModelForm, kad sukurtumėte registracijos formą.
# • Įtraukite papildomą patikrą – jei vartotojas bando užsiregistruoti su jau
# egzistuojančiu el. paštu, parodykite klaidą formoje.
# Vaizdai (views)
# • Sukurkite du atskirus vaizdus:
# o Vienas puslapis registracijai (forma su POST apdorojimu)
# o Kitas puslapis, kuris rodo visų užsiregistravusių asmenų sąrašą
# Šablonai
# • Registracijos forma turi turėti CSRF apsaugą
# • Formoje turi būti rodomi klaidų pranešimai, jei naudotojas pateikia netinkamus
# duomenis
# • Dalyvių sąrašo puslapyje turi būti aiškiai atvaizduoti visi registruoti žmonės (vardas,
# el. paštas, registracijos data)
# Maršrutai (URLs)
# • Sukurkite du URL adresus:
# o /registracija/ – registracijos forma
# o /dalyviai/ – visų registruotų vartotojų sąrašas
# Funkcionalumo santrauka:
# • Vartotojas užpildo formą su vardu ir el. paštu.
# • Jei forma pateikta teisingai – naudotojas peradresuojamas į dalyvių sąrašą.
# • Jei su tuo el. paštu jau yra registracija – rodomas klaidos pranešimas.
# • Duomenys saugomi duomenų bazėje.
# • Adminas gali matyti visus užsiregistravusius žmones.





from django.db import models

class Vartotojas(models.Model):
    vardas = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sukurta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vardas} ({self.email})'
