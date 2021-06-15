from django.shortcuts import render, redirect
from crud.models import Student, Blog, Action
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def index(request):
    return render(request, "index.html")


def profile(request):
    user = request.user
    if request.method == 'POST':
        blog = Blog()
        if request.user.is_authenticated:
            if request.POST.get('name') != "" and request.POST.get('title') != "" and request.POST.get('desc') != "" and len(request.FILES) != 0:
                blog.name = request.POST.get("name")
                blog.title = request.POST.get("title")
                blog.desc = request.POST.get("desc")
                blog.image = request.FILES['image']
                blog.likes = 0
                blog.dislikes = 0
                blog.user_id = user.id
                blog.save()
                return redirect('profile')
            else:
                print("error")
        else:
            print("user is not auth")
    blog = Blog.objects.filter(user_id=user.id)
    return render(request, "profile.html", {"data": blog})


def blog(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", {"data": blog})


def blogs(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "blogs.html", {"data": blog})


def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    if len(blog.image) > 0:
        os.remove(blog.image.path)
    blog.delete()
    return redirect('profile')


def crud(request):
    if request.method == "POST":
        student = Student()
        if request.POST.get("name") != "" and request.POST.get("age") != "" and request.POST.get("gender") != "SELECT":
            student.name = request.POST.get("name")
            student.age = request.POST.get("age")
            student.gender = request.POST.get("gender")
            student.save()
    data = Student.objects.all()
    return render(request, "crud.html", {"datas": data})


def crudDelete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("crud")


def login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get(
            "email"), password=request.POST.get("password"))
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return redirect('crud')
    return redirect("index")


def signin(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST.get(
            "email"), password=request.POST.get("password"))
        user.first_name = request.POST.get("name")
        user.save()
        return redirect("blog")
    return redirect("index")


def logout(request):
    auth_logout(request)
    return redirect("index")


def likes(request):
    if request.method == "POST":
        blog_id = request.POST.get('blog_id')
        blog = Blog.objects.get(id=blog_id)
        blog_likes = blog.likes
        action = Action.objects.filter(blog_id=blog_id, email=request.user)
        print(action)
        if action.exists():
            print("else")
        else:
            blog_likes = blog_likes + 1
            blog.likes = blog_likes
            blog.save()
            newAction = Action()
            newAction.email = request.user
            newAction.blog_id = blog_id
            newAction.save()
        return redirect('blog')
    return redirect('blog')


def dislikes(request):
    if request.method == "POST":
        blog_id = request.POST.get('blog_id')
        blog = Blog.objects.get(id=blog_id)
        blog_dislikes = blog.dislikes
        action = Action.objects.filter(blog_id=blog_id, email=request.user)
        print(action)
        if action.exists():
            print("else")
        else:
            blog_dislikes = blog_dislikes + 1
            blog.dislikes = blog_dislikes
            blog.save()
            newAction = Action()
            newAction.email = request.user
            newAction.blog_id = blog_id
            newAction.save()
        return redirect('blog')
    return redirect('blog')
