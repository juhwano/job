from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm

def index(request):
    return render(request, 'common/index.html')