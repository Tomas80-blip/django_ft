# Puslapiavimas ir paieška (pagination & search)

# Tikslai
# Išmokti padalinti duomenis į puslapius naudojant Django Paginator klasę.
# Įgyvendinti paieškos funkcionalumą naudojant formą ir užklausos parametrus.
# Naudoti Q objektus sudėtingesniam filtravimui.

# Teorija

# Puslapiavimas

# Django turi integruotą Paginator klasę, kuri leidžia padalinti objektų sąrašą į kelis puslapius. Kiekvienas puslapis turi ribotą objektų skaičių, ir naudotojas gali pereiti tarp jų per ?page= užklausos parametrą.
#
# Pagrindinis veikimo principas:
#
# from django.core.paginator import Paginator
#
# objektai = Post.objects.all()
# paginator = Paginator(objektai, 5)  # 5 objektai per puslapį
#
# puslapio_numeris = request.GET.get('page')
# page_obj = paginator.get_page(puslapio_numeris)

# Šablone naudojama:
#
# {% for post in page_obj %}
#   <h2>{{ post.title }}</h2>
# {% endfor %}
#
# <div>
#   {% if page_obj.has_previous %}
#     <a href="?page={{ page_obj.previous_page_number }}">Ankstesnis</a>
#   {% endif %}
#
#   <span>Puslapis {{ page_obj.number }} iš {{ page_obj.paginator.num_pages }}</span>
#
#   {% if page_obj.has_next %}
#     <a href="?page={{ page_obj.next_page_number }}">Kitas</a>
#   {% endif %}
# </div>

# Paieška
# Paieška įgyvendinama per GET formą, kurioje naudotojas įveda raktažodį. Šis raktažodis naudojamas filtruoti duomenis vaizde (view).
#
# Paprastas pavyzdys:
#
# query = request.GET.get('q')
# if query:
#     objektai = Post.objects.filter(title__icontains=query)
# else:
#     objektai = Post.objects.all()
# Formos pavyzdys šablone:
#
# <form method="get">
#   <input type="text" name="q" placeholder="Ieškoti..." value="{{ request.GET.q }}">
#   <button type="submit">Ieškoti</button>
# </form>
# Q objektai
# Q objektai leidžia kurti sudėtingesnes filtravimo sąlygas, naudojant OR vietoje įprasto AND.
#
# from django.db.models import Q
#
# query = request.GET.get('q')
# if query:
#     objektai = Post.objects.filter(
#         Q(title__icontains=query) | Q(body__icontains=query)
#     )
# Tai naudinga, kai norime ieškoti pagal kelis laukus vienu metu.
#
# Praktika
# Sukurk ListView arba funkciją, kuri rodo visus įrašus naudodama Paginator (po 5 įrašus puslapyje).
# Pridėk paieškos formą (naudodamas GET metodą), kuri leidžia ieškoti pagal pavadinimą (title).
# Naudok Q objektą, kad būtų galima ieškoti tiek title, tiek body laukuose vienu metu.
# Pritaikyk paiešexitkos rezultatų filtravimą prieš perduodant objektus Paginator klasei.
# Šablone parodyk rezultatus, paieškos formą, navigacijos nuorodas tarp puslapių.
# Įsitikink, kad paieškos rezultatai ir puslapiavimas veikia kartu.
# Klausimai savikontrolei
# Kaip veikia Paginator klasė ir kodėl naudinga ją naudoti?
# Kuo skiriasi paginator.get_page() nuo paginator.page()?
# Kodėl naudinga naudoti GET formą paieškai, o ne POST?
# Kada naudoti Q objektus vietoje paprasto .filter()?
# Kaip užtikrinti, kad paieškos parametras išliktų perėjus tarp puslapių?

# per shell'a prideti 200 postu po kodo parasymo

# python manage.py shell

# >> > from app.models import Post
# >> > for i in range(1, 201):
#         Post.objects.create(title=f'Postas Nr. {i}', body=f'Tai yra posto body Nr. {i}')
# exit
# ir python manage.py runserver

# arba
# pvz kaip supostinti 200 irasu su SHELL

# def super_loop():
#     from app.models import Post#
#     for i in range(1, 201):
#         Post.objects.create(
#             title=f'Postas Nr. {i}',
#             body=f'Tai yra posto body Nr. {i}'
#         )

