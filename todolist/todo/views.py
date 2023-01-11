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
        # return render(request, "todo/index.html",{'todos':todo})
        return redirect('/')
    return render(request, "todo/index.html", {'todos':todo})

def delete(request, pk):
    todo = Todo.objects.all()
    del_todo = Todo.objects.get(id=pk)#This looks for object id you clicked on and then looks to delete it
    del_todo.delete()#This deletes from the db
    return redirect('/')