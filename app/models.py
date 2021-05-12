from django.db import models


# Create your models here.
class Stores(models.Model):
    objects = None
    name = models.CharField(max_length=150)
    storeName = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    district = models.CharField(max_length=120)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
