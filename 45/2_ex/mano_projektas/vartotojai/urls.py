from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('registracija/', views.registracija, name='registracija'),
    path('prisijungti/', LoginView.as_view(template_name='vartotojai/prisijungti.html'), name='prisijungti'),
    path('atsijungti/', LogoutView.as_view(), name='atsijungti'),
    path('profilis/', views.profilis, name='profilis'),
    path('redaguoti/', views.redaguoti_profili, name='redaguoti_profili'),
    path('naudotojai/', views.naudotoju_sarasas, name='naudotoju_sarasas')
]