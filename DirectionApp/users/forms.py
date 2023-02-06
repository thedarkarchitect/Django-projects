from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserForm(UserCreationForm):
    """
    this form uses built-in UserCreationForm to handle user creation
    """
    first_name = forms.CharField(max_length=200, required=True,widget=forms.TextInput(attrs={'placeholder':'*Your first name...'}))
    last_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your last name...'}))
    username = forms.EmailField(max_length=300, required=True, widget=forms.TextInput(attrs={'placeholder':'*Email..'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*Password...'}))
    password2 =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'*Confirm Password...'}))

    #token for the reCaptcha
    token = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

class AuthForm(AuthenticationForm):
    """
    this form uses bulit-in AuthenticationForm to handle user auth
    """

    username = forms.EmailField(max_length=300, required=True, widget=forms.TextInput(attrs={'placeholder':'*Email..'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'*Password..'}))

    class Meta:
        model = User
        fields = '__all__'

class UserProfileForm(forms.ModelForm):#this form is going to base on the Userprofile model
    """
    this is a Basic model-form for our user profile that extends Django user model
    """
    
    address = forms.CharField(max_length=200, required=True, widget=forms.HiddenInput())
    town = forms.CharField(max_length=200, required=True, widget= forms.HiddenInput())
    county = forms.CharField(max_length=200, required=True, widget= forms.HiddenInput())
    post_code = forms.CharField(max_length=200, required=True, widget= forms.HiddenInput())
    county = forms.CharField(max_length=200, required=True, widget= forms.HiddenInput())
    longitude = forms.CharField(max_length=200, required=True, widget= forms.HiddenInput())
    latitude = forms.CharField(max_length=200, required=True, widget= forms.HiddenInput())

    class Meta:
        model = UserProfile
        fields = (
            'address', 'town', 'county', 'post_code', 'country', 'longitude', 'latitude'
        )