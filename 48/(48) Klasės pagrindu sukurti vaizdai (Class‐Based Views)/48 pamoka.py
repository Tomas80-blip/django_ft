# Klasės pagrindu sukurti vaizdai (Class-Based Views)
# Tikslai
# Suprasti, kuo klasės pagrindu kuriami vaizdai (CBV) skiriasi nuo funkcinių vaizdų (FBV).
# Išmokti naudoti ListView, DetailView, CreateView, UpdateView, DeleteView.
# Suprasti, kaip naudoti get_context_data() papildomiems duomenims perduoti į šabloną.
# Naudoti success_url nurodant, kur peradresuoti po sėkmingos operacijos.
# Teorija
# Kuo skiriasi FBV ir CBV?
# Funkciniai vaizdai (Function-Based Views) – tai įprastos Python funkcijos, kurios apdoroja užklausą ir grąžina atsakymą.
#
# Klasiniai vaizdai (Class-Based Views, CBV) – tai Python klasės, kurios paveldi iš django.views ir leidžia naudoti objektinį požiūrį.
#
# CBV padeda sutrumpinti kodą, ypač kai kuriamos CRUD operacijos (sukurti, peržiūrėti, redaguoti, ištrinti objektus).
#
# Dažniausiai naudojamos CBV klasės
# ListView – objektų sąrašo atvaizdavimas
# DetailView – vieno objekto detalus vaizdas
# CreateView – naujo objekto kūrimas
# UpdateView – esamo objekto redagavimas
# DeleteView – objekto ištrynimas
# Pavyzdys: ListView
# from django.views.generic import ListView
# from .models import Post
#
# class PostListView(ListView):
#     model = Post
#     template_name = 'post_list.html'
#     context_object_name = 'posts'
# DetailView
# from django.views.generic import DetailView
#
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'
# CreateView ir UpdateView
# from django.views.generic.edit import CreateView, UpdateView
# from django.urls import reverse_lazy
#
# class PostCreateView(CreateView):
#     model = Post
#     fields = ['title', 'body']
#     template_name = 'post_form.html'
#     success_url = reverse_lazy('post_list')
#
# class PostUpdateView(UpdateView):
#     model = Post
#     fields = ['title', 'body']
#     template_name = 'post_form.html'
#     success_url = reverse_lazy('post_list')
# DeleteView
# from django.views.generic.edit import DeleteView
#
# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'post_confirm_delete.html'
#     success_url = reverse_lazy('post_list')
# get_context_data()
# Jeigu reikia papildomų duomenų šablonui, galima perrašyti get_context_data() metodą:
#
# class PostListView(ListView):
#     model = Post
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['kintamasis'] = 'Papildoma info'
#         return context
# Praktika
# Sukurk ListView ir DetailView, kurie rodo įrašų sąrašą ir atskirus įrašus.
# Sukurk CreateView, UpdateView ir DeleteView, kurie leidžia atlikti visas CRUD operacijas.
# Įrašyk maršrutus į urls.py, panaudodamas as_view() metodą.
# from django.urls import path
# from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
#
# urlpatterns = [
#     path('', PostListView.as_view(), name='post_list'),
#     path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
#     path('naujas/', PostCreateView.as_view(), name='post_create'),
#     path('<int:pk>/redaguoti/', PostUpdateView.as_view(), name='post_update'),
#     path('<int:pk>/istrinti/', PostDeleteView.as_view(), name='post_delete'),
# ]
# Sukurk atitinkamus šablonus: post_list.html, post_detail.html, post_form.html, post_confirm_delete.html.
# Patikrink, ar veikia naujo objekto kūrimas, redagavimas, peržiūra ir ištrynimas.
# Klausimai savikontrolei
# Kuo skiriasi CBV nuo FBV ir kada verta naudoti CBV?
# Kam naudojamas success_url?
# Kaip pritaikyti get_context_data() konkretiems poreikiams?
# Kokiais atvejais CBV tampa efektyvesni už funkcinius vaizdus?
# Kodėl reverse_lazy naudojamas vietoje reverse CBV kontekste?
# Pages 30
# Find a page…
# Home
# Pamoka 23 SQL naudojimas Jupyter Notebook ir Db Browser SQLite
# Pamoka 24 Darbas su keliomis SQL lentelėmis
# Pamoka 25 Duomenų bazės projektavimas, constraints
# Pamoka 26 SQL Saugumas ir SQL Injection Atakos
# Pamoka 27 SQL Santykiai: One‐to‐Many ir Many‐to‐Many
# Pamoka 28
# Pamoka 29 Flask pagrindai – maršrutai, šablonai ir formos
# Pamoka 30 Flask ir SQLAlchemy – duomenų bazės valdymas
# Pamoka 31
# Pamoka 32 Kelių lentelių naudojimas Flask su SQLAlchemy
# Pamoka 33 React įvadas
# Pamoka 34 useState hook
# Pamoka 35 useEffect ir API užklausos
# Pamoka 36 React Router pagrindai
# Clone this wiki locally
# https://github.com/DariusDaskevicius/full_stack_ft_2.wiki.git
# Footer
# © 2025 GitHub, Inc.