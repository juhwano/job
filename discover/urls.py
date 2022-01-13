from django.urls import path, include
from . import views

app_name='discover'

urlpatterns = [
    path('', views.index, name='index')
]