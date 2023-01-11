from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo = Todo.objects.all()#This access' all objects in the db

    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title'] #saving what is input in the variable title
        )
        new_todo.save()
        return render(request, "todo/index.html",{'todos':todo})
    return render(request, "todo/index.html", {'todos':todo})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')