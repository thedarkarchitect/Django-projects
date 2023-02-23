from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login


# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()#you put the current user into a variable to handle them specifically if need be
            login(request, user)#this authenticated user

            return redirect('frontpage')
    else:
        form = SignUpForm()

    context = {
        'form' : form
    }

    return render(request, 'core/signup.html', context)