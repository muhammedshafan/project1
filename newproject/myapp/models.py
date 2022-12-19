from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, null=True)
    address = models.TextField(max_length=500, null=True)

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    course = models.CharField(max_length=300)
    roll_no = models.CharField(max_length=200)
    address = models.TextField(max_length=200)