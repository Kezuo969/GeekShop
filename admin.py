from django.contrib import admin
from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory, Product)

# Register your models here.
