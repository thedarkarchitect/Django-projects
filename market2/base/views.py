from django.shortcuts import render, redirect
from items.models import Category, Item
from .forms import SignUpForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]#this will show the products that are not solded the first 6 of them from the items db
    categories = Category.objects.all()#this will show all and let you have access the categories 

    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'base/index.html', context)

def contact(request):
    return render(request, 'base/contact.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()

            return redirect('/')
    else:
        form = SignUpForm()


    context = {
        'form' : form
    }

    return render(
        request, 'base/signup.html',
        context
    )