from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# Create your views here.
def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers':customers,
        'total_orders' : total_orders,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {
        'products': products
    })

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()#this will show the orders of the customer with the id

    context = {
        'customer': customer,
        'orders': orders
    }
    return render(request, 'accounts/customer.html', context)

def createOrder(request):
    form = OrderForm()

    if request.method == 'POST': #this checks if the method of the form is actually POST
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form
    }

    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)#this to populate the form using the item clicked on
    
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)#if the form is Posted with the prepopulate order information and its satisfactory
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form
    }
    return render(request, 'accounts/order_form.html', context)

def delete(request, pk):
    order = Order.objects.get(id=pk)
    item = order.product

    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {
        'item': item
    }

    return render(request, 'accounts/delete.html', context)