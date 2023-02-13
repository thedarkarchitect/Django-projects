from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_Cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()

    context = {
        'products' : products,
        'cartItems' : cartItems
    }
    return render(request, 'store/store.html', context) 

def cart(request):

    if request.user.is_authenticated:#will check if the customer is signed in and authenticated to accesss the cart of the specific customer
        customer = request.user.customer#accessing the customer thru the user and customer one to one relationship
        #this will allow to create an order or set an order
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()#this helps query child objects from parent in small caps from order class to all the items
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total' : 0, 'get_Cart_items': 0 }
        cartItems = order['get_Cart_items']

    context = {
        'items':items,
        'order':order,
        'cartItems': cartItems
        }
    return render(request, 'store/cart.html', context) 

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        #create empty cart for now for none-logged in users
        order = { 'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        items = []
        cartItems = order['get_cart_items']

    context = {
        'items':items,
        'order':order,
        'cartItems' : cartItems
        }
    return render(request, 'store/checkout.html', context) 

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
    return JsonResponse('Payment submitted..', safe=False )