from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("blogs", views.blog, name="blog"),
    path("blogs/<int:id>", views.blogs, name="blogs"),
    path("delete_blog/<int:id>", views.delete_blog, name="delete_blog"),
    path("crud", views.crud, name="crud"),
    path("deletestud/<int:id>", views.crudDelete, name="sdelete"),

]
