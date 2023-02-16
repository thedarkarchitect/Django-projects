from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *
from .forms import StudentForm


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

def add(request):
    #db data must be manipulated using a 
    # form  = StudentForm()#unbound form
    if request.method == 'POST':
        form = StudentForm(request.POST)#bound form 
        if form.is_valid():
            #pulling data from the form data dictionary called cleaned data and at this point validated data 
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa
            )
            
            # form.save()instead
            new_student.save()

            context = {
                'form': StudentForm(),
                'success': True,
            }

            return render(request, 'student/add.html', context)
            
    else:
        #otherwise display an empty form
        form = StudentForm()

    context = {
        'form': form
        }
    return render(request, 'student/add.html', context)

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)#GETS The specific student to edit
        form = StudentForm(request.POST, instance=student)#this fills form with that student to edit
        if form.is_valid():
            form.save()

            context = {
                'form':form,
                'success': True
            }

            return render(request, 'student/edit.html', context)
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST)

    context = {
        'form':form
    }
    return render(request, 'student/edit.html', context)

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))#this will help us not to create or hardcode a url but have url that performs a task
