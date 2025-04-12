from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dalyviai/registracija/', views.register_form_view, name='register'),
    path('dalyviai/', views.vartotojai_list_view, name='vartotojai_list')
]