from django.shortcuts import render

# Create your views here.
def index(request):
    context = {

    }
    
    return render(request, 'posts/index.html', context)

def about(request):
    return render(request, 'posts/about.html')

def contact(request):
    return render(request, 'posts/contact.html')

def post(request):
    return render(request, 'posts/post.html')