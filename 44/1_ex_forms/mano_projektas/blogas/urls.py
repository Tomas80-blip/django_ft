from django.urls import path
from . import views

urlpatterns = [
    path('', views.naujas_irasas, name='pagrindinis'),
    path('naujas/', views.naujas_irasas, name='naujas'),
    path('kontaktai/', views.kontaktai, name='kontaktai'),
]