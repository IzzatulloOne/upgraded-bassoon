from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    products = models.Product.objects.all()
    context = {
        'product' : products
    }
    return render(request, 'index.html', context)