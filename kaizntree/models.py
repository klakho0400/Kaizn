from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class Item(models.Model):
    sku = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    stock_status = models.FloatField()
    available_stock =  models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)