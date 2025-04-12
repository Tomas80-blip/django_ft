# Django administracinė sąsaja (admin)
# Tikslai
# Suprasti, kokią reikšmę turi administracinė sąsaja Django projektuose.
# Išmokti aktyvuoti ir pritaikyti admin sistemą.
# Suprasti, kaip modeliai pateikiami administracinėje aplinkoje.
# Pradėti konfigūruoti, kaip duomenys atvaizduojami ir tvarkomi administracinėje aplinkoje.
# Teorija
# Kas yra Django administracinė sąsaja
# Django turi įdiegtą universalią administravimo sistemą, kuri leidžia valdyti duomenis
# grafinėje vartotojo sąsajoje be būtinybės rašyti SQL užklausų ar naudotis išorine
# duomenų bazių valdymo sistema.
#
# Ji suteikia:
#
# Modelių įrašų kūrimą, redagavimą ir šalinimą.
# Paiešką ir filtravimą.
# Puslapių rūšiavimą pagal laukus.
# Teisių valdymą skirtingiems vartotojams.
# Django administracinė sąsaja naudoja tuos pačius modelius, kuriuos kuriame models.py faile.
#
# Kaip įjungti administracinę sistemą
# Registruoti modelius admin.py faile, naudojant admin.site.register():
# from django.contrib import admin
# from .models import Post
#
# admin.site.register(Post)
# Sukurti administratorių naudojant komandą terminale:
# python manage.py createsuperuser
# Sistema paprašys įvesti naudotojo vardą, el. paštą ir slaptažodį.
#
# Prisijungti prie admin aplinkos adresu http://127.0.0.1:8000/admin ir įvesti prisijungimo duomenis.
# Jeigu viskas atlikta teisingai, matysime registruotus modelius kaip lenteles su galimybe juos kurti,
# redaguoti ir šalinti.
#
# Modelių vaizdavimo konfigūravimas
# Kad administracinėje sąsajoje būtų galima patogiai matyti informaciją, galima naudoti ModelAdmin klasę.
# Ji leidžia nurodyti, kokie laukai rodomi sąrašo vaizde.
#
# Pavyzdys:
#
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#
# admin.site.register(Post, PostAdmin)
# Papildomos ModelAdmin savybės:
#
# search_fields – leidžia ieškoti pagal konkrečius laukus
# list_filter – prideda filtravimo šoninius laukelius
# ordering – nurodo pirminį įrašų rikiavimą
# Praktika
# Patikrink, ar tavo modelis Post yra užregistruotas admin.py faile. Jei ne – įtrauk jį naudodamas admin.site.register().
#
# Sukurk supernaudotoją naudodamas komandą:
#
# python manage.py createsuperuser
# Prisijunk prie administracinės sąsajos adresu http://127.0.0.1:8000/admin.
#
# Sukurk bent vieną įrašą modelyje Post naudodamasis admin sąsaja.
#
# Sukurk PostAdmin klasę ir naudok list_display, kad atvaizduotum bent du
# stulpelius sąrašo rodinyje (pvz. title ir created_at).
#
# Pridėk paieškos funkcionalumą naudodamas search_fields, pavyzdžiui:
#
# search_fields = ('title',)
# Išbandyk įrašų filtravimą, rūšiavimą ir redagavimą administracinėje dalyje.
# Klausimai savikontrolei
# Kuo naudinga naudoti Django administracinę sistemą vietoje tiesioginio darbo per duomenų bazės įrankius?
# Kokios informacijos reikia, norint sukurti supernaudotoją?
# Kaip pakeisti, kokie stulpeliai rodomi administracinio sąrašo lange?
# Kaip būtų galima greitai rasti konkretų įrašą admin sąsajoje, jei jų yra šimtai?
# Koks būtų veiksmų planas, jeigu reikia suteikti prieigą tik prie tam tikros modelio dalies kitam naudotojui?