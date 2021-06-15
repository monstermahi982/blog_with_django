from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.profile, name="profile"),
    path("blogs", views.blog, name="blog"),
    path("blogs/<int:id>", views.blogs, name="blogs"),
    path("delete_blog/<int:id>", views.delete_blog, name="delete_blog"),
    path("crud", views.crud, name="crud"),
    path("deletestud/<int:id>", views.crudDelete, name="sdelete"),
    path("login", views.login, name="login"),
    path("signin", views.signin, name="signin"),
    path("logout", views.logout, name="logout"),
    path("likes", views.likes, name="likes"),
    path("dislikes", views.dislikes, name="dislikes"),
]
