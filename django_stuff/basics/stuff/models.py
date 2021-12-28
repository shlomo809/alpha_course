from django.db import models

# Create your models here.



class People(models.Model):
    name = models.CharField(max_length=100)
    personal_id = models.IntegerField(primary_key=True)
    birth_date = models.CharField(max_length=20) 


    