from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.pagrindinis, name='pagrindinis'),
    path('registracija/', views.registracija, name='registracija'),
    path('prisijungti/', LoginView.as_view(template_name='vartotojai/prisijungti.html'), name='prisijungti'),
    path('atsijungti/', LogoutView.as_view(), name='atsijungti'),
    path('slaptas/', views.slaptas, name='slaptas'),
]
