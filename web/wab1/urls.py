from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "home"),
    path("wab1/", views.index2, name = "index2"),



]