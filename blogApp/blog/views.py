from django.db.models import Q #used to search in multiple fields
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm

# Create your views here.
def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)#this will return post or a 404 if post not found

    #this method below is tringer when the submit button is hit to send the data from comments to the database.
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #the steps below are done to avoid a crash caused by the foreign key
            comment = form.save(commit=False)
            comment.post = post#this relates to the post at line 7
            comment.save()#saved to the database
            return redirect('detail', slug=slug)#return you to the detail page of the same instance of the blog post
    else:
        form = CommentForm()

    context = {
        'post' : post,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    context = {
        'category' : category,
        'posts':posts
    }
    return render(request, 'blog/category.html', context)

def search(request):
    query = request.GET.get('query', '') #this allows you to get ehat is passed into the empty string
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))#this goes to the databse and pulls what is passed to the query 
    
    context={
        'posts' : posts
    }
    return render(request, 'blog/search.html', context)
