from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy #helps redirect too aspecific page after submission of a 

from django.contrib.auth.views import LoginView

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(ListView):#this view displays the database contents
    model = Task
    context_object_name = 'tasks'#this allows us to tap into the database using the context name as a variable('tasks')


class TaskDetail(DetailView):#this view shows the database contents in detail
    model = Task
    context_object_name = 'task' #customize the reference object name in htmls
    #customize the template name
    #template_name = 'base/task.html'

class TaskCreate(CreateView):#this views allows user to create an item then save it to the database and redirect ot the Tasklist view
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks') #redirects user to the tasks page after creation of task

class TaskUpdate(UpdateView):#similar to the create view but all it does return the model prefilled for edittin
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

