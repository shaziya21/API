from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    city = models.CharField(max_length=200)
    passby = models.CharField(max_length=200)
    # passby m teacher ka name ho skta h jo pass krega ya jis teacher ne kn kn se student ka result check kri h etc 
