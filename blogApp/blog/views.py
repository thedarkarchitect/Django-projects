from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

# Create your views here.
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)#this will return post or a 404 if post not found

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
