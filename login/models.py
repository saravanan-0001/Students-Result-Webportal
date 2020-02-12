import csv
from django.db import models
from postgres_copy import CopyManager

# Create your models here.
class Login(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    
    


class Marks(models.Model):
    rollnum=models.IntegerField(default=0)
    name=models.CharField(max_length=100)
    c=models.IntegerField(default=0)
    ds=models.IntegerField(default=0)
    m3=models.IntegerField(default=0)
    architecture=models.IntegerField(default=0)
    dsp=models.IntegerField(default=0)    
    fname=models.FileField()