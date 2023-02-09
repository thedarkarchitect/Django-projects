from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
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
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')