from django.shortcuts import render, redirect
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
    #this prepopulates the form
    movie = Movie.objects.get(pk=pk)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        movie = Movie.objects.get(pk=pk)
        form = MovieForm( instance=movie)
        if form.is_valid():
            form.save()
        return redirect('index')
    
    context = {
        'movie':movie,
        'form':form
    }
    return render(request, 'movie/update.html', context)

def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=id)
        movie.delete()
        return redirect('index')