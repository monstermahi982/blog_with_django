from django.shortcuts import render, redirect
from crud.models import Student


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


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
