from django.shortcuts import render
def index (request):
    return render(request, "mainapp/index.html")

def products (request):
    return render(request, "mainapp/products.html")

from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):
    return render(request, 'mainapp/index.html')


def products(request, id=None):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)

def product(request, pk):
    title = "продукты"
    content = {
        "title": title,
        "links_menu": get_links_menu(),
        "product": get_product(pk),
        "media_url": settings.MEDIA_URL,
    }


    return render(request, "mainapp/product.html", content)
# Create your views here.
