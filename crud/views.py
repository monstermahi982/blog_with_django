from django.shortcuts import render, redirect
from crud.models import Student, Blog
import os


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    if request.method == 'POST':
        blog = Blog()
        if request.POST.get('name') != "" and request.POST.get('title') != "" and request.POST.get('desc') != "" and len(request.FILES) != 0:
            blog.name = request.POST.get("name")
            blog.title = request.POST.get("title")
            blog.desc = request.POST.get("desc")
            blog.image = request.FILES['image']
            blog.save()
        else:
            print("error")

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
    return redirect('blog')


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
