from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

tasks = []#this will take the tasks to do 

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")#the form field will take characters


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, 'tasks/indexT.html', {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)#this will input the inserted data into form using "request.POST"
        if form.is_valid():#if data entered is valid
            task = form.cleaned_data["task"]#this is var to hold task entered in field or hold all data entered
            tasks.append(task)#if the task is valid we put the task in the list
            return render(request, 'tasks/indexT.html', {"tasks": tasks})#after text is added return us to the index page
        else:
            #if the data is not valid we shall serve up the same form they had so they can correct errors
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()
    })