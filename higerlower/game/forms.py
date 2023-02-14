from django import forms 

class GuessForm(forms.Form):
    guess = forms.CharField()
