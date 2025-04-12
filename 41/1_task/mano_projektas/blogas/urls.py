from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagrindinis, name='pagrindinis'),
    path('kontaktai/', views.kontaktai, name='kontaktai'),
         # kelias^^,   ^^funkc. kuri bus vykdoma, ^^simbolinis vardas
    #                     iš views.py failo
    path('naujienos/', views.naujienos, name='naujienos'),
    path('apie/', views.apie, name='apie'),
    path('autorius/', views.autorius, name= 'autorius')
]

