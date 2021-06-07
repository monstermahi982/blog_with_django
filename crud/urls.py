from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("crud", views.crud, name="crud"),
    path("deletestud/<int:id>", views.crudDelete, name="sdelete"),

]
