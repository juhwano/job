from django.contrib import admin
from django.urls import path, include

from . import views
app_name = 'talk'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:postId>/', views.detail, name='detail'),
    path('answer/create/<int:postId>/', views.answer_create, name='answer_create')
]