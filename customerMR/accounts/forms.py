from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer 
        fields = '__all__'
        exclude = ['user'] 

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = '__all__' #all the fields in the Irder model
        fields = ['product', 'status']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
