"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("/", views.homepage, name="homepage"),
    path("internet/signup/", views.misc1, name="misc1"),
    path("signup/", views.signup, name="signup"),
    path("misc1/", views.misc1, name="misc1"),
    path("internet/misc1/", views.misc1, name="misc1"),
    path("misc2/", views.misc2, name="misc2"),
    path("internet/misc2/", views.misc2, name="misc2"),
]
