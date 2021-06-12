from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)


class Blog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, null=True)
    desc = models.TextField(max_length=250)
    date = models.DateField(auto_now=False, auto_now_add=True)
    image = models.ImageField(
        upload_to='uploads')
