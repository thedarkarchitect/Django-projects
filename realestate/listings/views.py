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
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form
    }

    return render(request, 'listing_create.html', context)