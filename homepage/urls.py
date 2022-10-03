from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),  # name parameter is to set name of url variable for template
]