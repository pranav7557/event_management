"""pasc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import *
from . import views

urlpatterns = [
    path('', views.signIn),
    path('postsign/', views.postsign),
    path('admin/', admin.site.urls),
    path('try/', func),
    path('search/', search, name="search"),
    path('events/', events, name="events"),
    path('register/', register, name="register"),
    path('data', data),
    path('att', update_att),
    path('add_data', add_data),
    path('menu', menu, name="menu"),
    path('login', signIn, name="login"),
    path('rep', rep),
    path('rep_', rep_),
]
