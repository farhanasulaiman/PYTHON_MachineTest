from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_student = models.BooleanField(default=False)


class Student(models.Model):
    user=models.ForeignKey('Login',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    phone = models.CharField(max_length=12)
    photo = models.FileField(upload_to='documents/')

    def __str__(self):
        return f'{self.name}'


class CollegeAdmin(models.Model):
    user=models.ForeignKey('Login',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone=models.CharField(max_length=12)


class Marks(models.Model):
    stud_id=models.ForeignKey('Student',on_delete=models.CASCADE)
    Science=models.CharField(max_length=30)
    Maths = models.CharField(max_length=30)
    Physics = models.CharField(max_length=30)
