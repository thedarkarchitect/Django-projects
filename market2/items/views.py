from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def browse(request):
    query = request.GET.get('query', '')#this will capture what is entered in the search bar input
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if  category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))#this will check if what is entered in the search bar is contained in items available

    context = {
        'items':items,
        'query':query,
        'categories':categories,
        'category_id': int(category_id)
    }

    return render(request, 'items/browse.html', context)


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)#a 404 will be loaded if the item is not found in the db
    #this will show related items of the same category that have not been sold showing only the first 3
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    context = {
        'item': item,
        'related_items':related_items
    }
    return render(request, 'items/detail.html', context)

@login_required
def new(request):
    form = NewItemForm()

    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)#request.FILES allows us to get the files the user uploads
        if form.is_valid():
            item = form.save(commit=False)#this allows you to submit to the database without showing created_by field
            item.created_by = request.user#this will stop the error by showing that we are authenticated

            item.save()#then the form will be saved
            return redirect('items:detail', pk=item.id)
            

    context ={
        'form':form,
        'title': 'New Item'
    }

    return render(request, 'items/form.html', context)


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    form = EditItemForm(instance=item)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)#request.FILES allows us to get the files the user uploads
        if form.is_valid():
            form.save()
            return redirect('items:detail', pk=item.id)
            

    context ={
        'form':form,
        'title': 'Edit Item'
    }

    return render(request, 'items/form.html', context)

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')