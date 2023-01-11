from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def word(request):
    search = request.GET.get('search')#this gets the word put in the search bar using the name of the input the search bar
    return render(request, "word.html" )