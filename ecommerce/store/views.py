from django.shortcuts import render
from .models import *
from django.http import JsonResponse

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
        order = {'get_cart_total' : 0, 'get_Cart__items': 0 }

    context = {
        'items':items,
        'order':order
        }
    return render(request, 'store/cart.html', context) 

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #create empty cart for now for none-logged in users
        order = { 'get_cart_total':0, 'get_cart_items':0}
        items = []

    context = {
        'items':items,
        'order':order
        }
    return render(request, 'store/checkout.html', context) 

def updateItem(request):
    return JsonResponse(
        'item was added', safe=False
    )