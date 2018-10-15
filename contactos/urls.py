from django.urls import path
from . import views


urlpatterns = [
    path('', views.contactos_index, name='index')
]