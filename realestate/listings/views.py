from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.
def listing_list(request):#this will list all the listings
    listings = Listing.objects.all()

    context = {
        'listings':listings
        }

    return render(request, 'listings.html', context)

def listing_retrieve(request, pk):#since we need to get a specific listing we shall need a pk to identify the specific listing
    listing = Listing.objects.get(id=pk)

    context = {
        'listing':listing
    }
    return render(request, 'listing.html', context)

def listing_create(request):
    form = ListingForm()

    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form
    }

    return render(request, 'listing_create.html', context)


def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)#this will get the specific lising form you want to update

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form
    }

    return render(request, 'listing_update.html', context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)#this will get the pk of the listing you click on 
    listing.delete()
    return redirect('/')