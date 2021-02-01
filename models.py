from django.db import models
from django.shortcuts import render


class ProductCategory (models.Model):
    name=models.CharField(max_length=64)
    text=models.TextField(unique=True, blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


def __str__(self):
    return self.name


def index (request):
    return render(request)

def __str__(self):
    return  (f'{self.name} | {self.category.name}')
