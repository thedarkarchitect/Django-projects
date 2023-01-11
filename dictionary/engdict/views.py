from django.shortcuts import render
from pydictionary import Dictionary

# Create your views here.
def index(request):
    return render(request, "index.html")

def word(request):
    search = request.GET.get('search')#this gets the word put in the search bar using the name of the input the search bar
    dictionary = Dictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)

    return render(request, "word.html" , {
        'meaning': meaning['Noun'][0],
        'synonyms': synonyms,
        'antonyms': antonyms
    })