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

    path("signup/", views.signup, name="signup"),
    path("internet/signup/", views.signup, name="signup"),

    path("car/", views.car, name="car"),
    path("internet/car/", views.car, name="car"),
    path("internet/internet/car/", views.car, name="car"),

    path("beauty/", views.beauty, name="beauty"),
    path("internet/beauty/", views.beauty, name="beauty"),
    path("internet/internet/beauty/", views.beauty, name="beauty"),

    path("art/", views.art, name="art"),
    path("internet/art/", views.art, name="art"),
    path("internet/internet/art/", views.art, name="art"),

    path("tech_science/", views.tech_science, name="tech_science"),
    path("internet/tech_science/", views.tech_science, name="tech_science"),
    path("internet/internet/tech_science/", views.tech_science, name="tech_science"),

    path("health/", views.health, name="health"),
    path("internet/health/", views.health, name="health"),
    path("internet/internet/health/", views.health, name="health"),

    path("entertainment/", views.entertainment, name="entertainment"),
    path("internet/entertainment/", views.entertainment, name="entertainment"),
    path("internet/internet/entertainment/", views.entertainment, name="entertainment"),

    path("sports/", views.sports, name="sports"),
    path("internet/sports/", views.sports, name="sports"),
    path("internet/internet/sports/", views.sports, name="sports"),

]
