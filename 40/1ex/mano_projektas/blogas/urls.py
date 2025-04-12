from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagrindinis, name='pagrindinis'),
    path('apie/', views.apie, name='apie'),
   # URL kelias^^,   ^^funkc. kuri bus vykdoma, ^^simbolinis vardas
    #                  iš views.py failo
]
