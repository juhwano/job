from django.urls import path, include
from . import views

app_name='discover'


urlpatterns = [
    path('', views.index, name='index'),
    path('get_data/', views.get_data, name='get_data'),
]