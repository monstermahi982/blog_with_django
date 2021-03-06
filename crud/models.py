from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)


class Blog(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, null=True)
    desc = models.TextField(max_length=250)
    date = models.DateField(auto_now=False, auto_now_add=True)
    image = models.ImageField(
        upload_to='uploads')
    user_id = models.CharField(max_length=50)
    likes = models.IntegerField()
    dislikes = models.IntegerField()


class Action(models.Model):
    email = models.CharField(max_length=50)
    blog_id = models.IntegerField()
