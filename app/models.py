from django.db import models

class Person(models.Model):
    name= models.CharField(max_length=90)
    age= models.IntegerField()
    pho= models.IntegerField()
    gender=models.CharField(max_length=20)
