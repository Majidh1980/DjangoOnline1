from django.shortcuts import render, redirect
from . import models

# Create your views here.

def Login(request):
    """
    #register
    product1 = models.product(name="noshabe", price=100, quantity= 100)
    product1.save()
    #update
    product.name = "chips"
    product.price = 250
    product.save()
    """
    products = models.product.objects.all()
    product = models.product.objects.filter(id=2).first()
    # product.delete()

    return render(request, 'index.html', context={'products':products})
def test(request):
    return render(request, 'test.html')

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        product = models.product(name=name, price=price, quantity=quantity)
        product.save()
        return redirect('login')


