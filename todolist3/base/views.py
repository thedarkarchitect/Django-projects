from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Task
from django.urls import reverse_lazy #helps redirect too aspecific page after submission of a 

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin#this retricts the user that enter the page
from django.contrib.auth.forms import UserCreationForm #Creates a user
from django.contrib.auth import login#signs in user directly after registering
# Create your views here.
class LoginViewPage(LoginView):
    template_name = 'base/login.html'#this locates the page that displays the login form 
    fields = '__all__'#this shows all the necessary fields for  the login 
    redirect_authenticated_user = True#this makes sure only registered user are let into the task form
    
    def get_success_url(self):
        return reverse_lazy('tasks')#this is a method that redirects the registered user to the tasks page url

class RegisterForm(FormView):
    template_name = 'base/register'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    

class TaskList(LoginRequiredMixin, ListView):#this view displays the database contents
    model = Task#This is the database
    context_object_name = 'tasks'#this allows us to tap into the database using the context name as a variable('tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)#this adds tasks to the loggedin user and shows the tasks of only the user logged in
        context['count'] = context['tasks'].filter(complete=False).count()#know how many tasks are not complete

        return context

class TaskDetail(LoginRequiredMixin, DetailView):#this view shows the database contents in detail
    model = Task
    context_object_name = 'task' #customize the reference object name in htmls
    #customize the template name
    #template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):#this views allows user to create an item then save it to the database and redirect ot the Tasklist view
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks') #redirects user to the tasks page after creation of task

    def form_valid(self, form):
        form.instance.user = self.request.user #confirms the user logged in and allows requests from the form of that user
        return super(TaskCreate, self).form_valid(form)#this allows us to continue with whatever the function class does

class TaskUpdate(LoginRequiredMixin, UpdateView):#similar to the create view but all it does return the model prefilled for edittin
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

