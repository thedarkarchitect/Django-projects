from django.shortcuts import render
from blog.models import Post

# Create your views here.

def frontpage(request):
    posts = Post.objects.all()

    context = {
        'posts':posts
    }

    return render(request, 'core/frontpage.html', context)

def about(request):
    return render(request, 'core/about.html')
