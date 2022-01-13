from django.urls import path
from django.contrib.auth import views as auth_views

from common import views

app_name = 'common'
from common import views

urlpatterns = [
    path('', views.index)
]