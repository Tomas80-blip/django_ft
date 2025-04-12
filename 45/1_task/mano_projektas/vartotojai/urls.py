from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from vartotojai.views import registracija, pagrindinis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registracija/', registracija, name='registracija'),
    path('prisijungti/', auth_views.LoginView.as_view(template_name='vartotojai/prisijungti.html'), name='prisijungti'),
    path('atsijungti/', auth_views.LogoutView.as_view(next_page='vartotojai/pagrindinis'), name='atsijungti'),
    path('', pagrindinis, name='pagrindinis'),
]