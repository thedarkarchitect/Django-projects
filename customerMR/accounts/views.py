from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, RegisterForm
from .filters import OrderFilter
# from django.contrib.auth.forms import UserCreationForm

#create login and restrictions
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, users_allowed, admin_only
#this show a flash message
from django.contrib import messages

# Create your views here.

#views for the login and registrations
@unauthenticated_user
def registerPage(request):
    #if we dont want the logged in user to see the login page or register page
    # if request.user.is_authenticated:
    #     return redirect('index')
    # else:
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            #get hold of user registering at that particular instance
            username = form.cleaned_data.get('username')

            # this will allow newly registered customers to be assigned to customer group automatically 
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, f"{username} has been created successfully")
            return redirect('loginPage')


    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
#we name is 'loginpage' so we don't have conflict with django login() method
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            #this will show a message if login creditials are wrong
            messages.info(request, 'Username Or Password is incorrect')

    context = {}
    return render(request, 'accounts/loginPage.html', context)

def userLogout(request):
    logout(request)
    return redirect('loginPage')

#views for the pages
@login_required(login_url='loginPage')#restricts access to every page decorator is on unless logged in
# @users_allowed(roles_allowed=['admin', ])
@admin_only
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

def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context) 

@login_required(login_url='loginPage')
@users_allowed(roles_allowed=['admin', ])
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {
        'products': products
    })

@users_allowed(roles_allowed=['admin', ])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()#this will show the orders of the customer with the id
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs #this will allow the orders to be searched using qs(queryset)

    context = {
        'customer': customer,
        'orders': orders,
        'myfilter': myfilter
    }
    return render(request, 'accounts/customer.html', context)

# @login_required(login_url='loginPage')
@users_allowed(roles_allowed=['admin', ])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=6)#extra shows the number of the fields shown

    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none() ,instance=customer)#queryset here will show only new fields without previous orders
    # form = OrderForm()

    if request.method == 'POST': #this checks if the method of the form is actually POST
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {
        'formset' : formset,
        'customer': customer
    }

    return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='loginPage')
@users_allowed(roles_allowed=['admin', ])
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

# @login_required(login_url='loginPage')
@users_allowed(roles_allowed=['admin', ])
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