from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'student_number':'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'Field_of_study': 'Major',
            'gpa': 'Enter GPA',
        }

        widget = {#customize the look of the forms
        'student_numbr': forms.NumberInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={ 'class': 'form-control'}) ,
        'last_name': forms.TextInput(attrs={ 'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'field_of_study': forms.TextInput(attrs={ 'class' : 'form-control'}),
        'gpa':forms.NumberInput(attrs={'class': 'form-control'}),
        }

