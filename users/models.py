from django.db import models

# Create your models here.

class User(models.Model):
    useremail = models.CharField(unique=True, max_length=30)
    userpw = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    age = models.DateField()
    gender=models.IntegerField()
    work_state=models.IntegerField()
    middle_level= models.CharField(null=True, max_length=30)
    join_date = models.DateField()
    withdrawal = models.IntegerField(null=True)
    withdrawal_date = models.DateField(null=True)

class MiddleCate(models.Model) :
    cateidx = models.IntegerField(unique=True)
    catename = models.CharField(max_length=30)