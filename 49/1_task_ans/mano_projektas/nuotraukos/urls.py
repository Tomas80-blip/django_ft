from django.urls import path
from .views import ikelti_nuotrauka

urlpatterns = [
    path('', ikelti_nuotrauka, name='ikelti_nuotrauka')
]

