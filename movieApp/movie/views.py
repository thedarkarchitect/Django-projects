from django.shortcuts import render
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movie/index.html', context)

def info(request, id):
    movies = Movie.objects.get(pk=id)

    context={
        'movies':movies
    }
    return render(request, 'movie/info.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    form = MovieForm(instance=movie)
    context = {
        'movie':movie,
        'form':form
    }
    return render(request, 'movie/update.html', context)