from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movie/index.html', context)

def edit(request):
    context={}
    return render(request, 'movie/edit.html', context)