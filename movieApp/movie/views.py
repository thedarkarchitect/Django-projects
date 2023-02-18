from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movie/index.html', context)

def edit(request, id):
    movies = Movie.objects.get(pk=id)
    context={
        'movies':movies
    }
    return render(request, 'movie/edit.html', context)