"""MLserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
import users.views

urlpatterns = [
    path('signup', users.views.signup),
    path('signup2', users.views.signup2),
    path('signin', users.views.signin),
    path('info/<id>', users.views.userinfo),
    path('update/<id>', users.views.userupdate),
    path('update2', users.views.userupdate2),
    path('delete/<id>', users.views.userdelete),
    path('delete2', users.views.userdelete2),
    path('logout', users.views.logout)
]
