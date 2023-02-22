from django.shortcuts import render
from blog.models import Post

# Create your views here.

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)#this is going to filter the posts shown according to the choices

    context = {
        'posts':posts
    }

    return render(request, 'core/frontpage.html', context)

def about(request):
    return render(request, 'core/about.html')

