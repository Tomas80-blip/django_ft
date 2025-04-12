from django.urls import path
from . import views

urlpatterns = [
    path('registacija/', views.registracija_view, name='registracija'),
    path('dalyviai/', views.dalyviai_view, name='dalyviai'),
]
