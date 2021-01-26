from django.shortcuts import render
def index (request):
    return render(request, "mainapp/index.html")

def products (request):
    return render(request, "mainapp/products.html")

def test_context (request):
    return render (request, "mainapp/context.html')

# Create your views here.
