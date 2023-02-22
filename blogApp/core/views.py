from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse

# Create your views here.

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)#this is going to filter the posts shown according to the choices

    context = {
        'posts':posts
    }

    return render(request, 'core/frontpage.html', context)

def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        "user=Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")