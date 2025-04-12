from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('registracija/', views.register, name='register'),
    path('prisijungti', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('atsijungti/', auth_views.LogoutView.as_view(), name='logout'),
]
