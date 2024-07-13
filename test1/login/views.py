from django.shortcuts import render
from . import models

# Create your views here.

def Login(request):
    product1 = models.product(name="noshabe", price=100, quantity= 100)
    product1.save()
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

