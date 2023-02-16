from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    students = Student.objects.all()

    context = {
        'students' : students
    }
    return render(request, 'student/index.html', context)

def view_student(request, id):
    student = Student.objects.get(pk=id)#this means get me a student whose primary key in the db is passed as the id of the student clicked
    return HttpResponseRedirect(reverse('index'))