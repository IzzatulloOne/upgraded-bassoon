from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=22)
    dateil = models.TextField()
    price = models.FloatField(max_length=30)
    image = models.ImageField(upload_to='product_images/')
