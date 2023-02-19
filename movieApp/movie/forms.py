from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'review', 'rating', 'description', 'img_url']

    labels = {
        'title': 'Enter title',
        'year' : 'Enter Year',
        'rating' : 'Enter rating',
        'description' : 'Enter description',
        'img_url' : 'Enter img url'
    }

    widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'year' : forms.TextInput(attrs={'class': 'form-control'}),
        'review': forms.TextInput(attrs={'class':'form-control'}),
        'rating': forms.NumberInput(attrs={'class':'form-control'}),
        'description': forms.Textarea(attrs={'class':'form-control'}),
        'img_url': forms.Textarea(attrs={'class':'form-control'})
    }