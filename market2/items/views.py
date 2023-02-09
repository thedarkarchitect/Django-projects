from django.shortcuts import render, get_object_or_404
from .models import Item

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