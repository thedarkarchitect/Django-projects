from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()

    context = {
        'products':products
    }
    return render(request, 'store/store.html', context) 

def cart(request):

    if request.user.is_authenticated:#will check if the customer is signed in and authenticated to accesss the cart of the specific customer
        customer = request.user.customer#accessing the customer thru the user and customer one to one relationship
        #this will allow to create an order or set an order
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()#this helps query child objects from parent in small caps from order class to all the items
    else:
        items = []

    context = {'items':items}
    return render(request, 'store/cart.html', context) 

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context) 