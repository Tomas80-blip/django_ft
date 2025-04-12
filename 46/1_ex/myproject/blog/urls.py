from django.urls import path
from . import views


#atvaizduoja posta
urlpatterns = [
    path('post/<int:post_id>/', views.post_detail, name='post_detail')
]
