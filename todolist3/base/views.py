from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Task
from django.urls import reverse_lazy #helps redirect too aspecific page after submission of a 

# Create your views here.
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