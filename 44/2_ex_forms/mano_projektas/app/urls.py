from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('atsiliepimai/naujas/', views.feedback_form_view, name='feedback_form'),
    path('atsiliepimai/', views.feedback_list_view, name='feedback_list'),
]
