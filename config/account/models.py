from django.db import models

# Create your models here.

class Person(models.Model):
    FName = models.CharField(name='firstname',max_length=30)
    LName = models.CharField(name='lastname',max_length=50)
    Age = models.IntegerField(name='age',max_length=3,null=True,blank=True)
# Id , FName, Lname ,age

class Addres(models.Model):
    pass

class Product(models.Model):
    pass
