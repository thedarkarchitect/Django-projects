from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

# Create your views here.
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)#this will return post or a 404 if post not found
    form = CommentForm()
    context = {
        'post' : post,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)
