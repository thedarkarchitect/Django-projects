from django.shortcuts import render, redirect
import random as rand 
from .forms import GuessForm


# Create your views here.
number = rand.randint(0, 9)
guesses = []

def index(request):
    form = GuessForm()

    if request.method == 'POST':
        form = GuessForm(request.POST)
        if form.is_valid():
            # form.save() only save the form if it's going to the database
            guess = form.cleaned_data['guess']
            guesses.append(guess)
            return redirect('/result/')
    
    context = {
        'number': number,
        'form': form,
        }
    return render(request, 'index.html', context)

def result(request):
    print(guesses)
    guess = int(guesses[-1])
    answer = ""
    
    if guess == number:
        answer = "green"
    elif guess > number:
        answer = "blue"
    else:
        answer = "red"


    context = {
        'guess': guess,
        'number': number,
        'answer':answer
    }
    return render(request, 'result.html', context)
