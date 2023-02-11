from django.shortcuts import render
from .models import Listing

# Create your views here.
def listing_list(request):#this will list all the listings
    listings = Listing.objects.all()

    context = {
        'listings':listings
        }

    return render(request, 'listings.html', context)

def listing_retrieve(request, pk):#since we need to get a specific listing we shall need a pk to identify the specific listing
    listing = Listing.objects.get(id=id)

    context = {
        'listing':listing
    }
    return render(request, 'listing.html', context)