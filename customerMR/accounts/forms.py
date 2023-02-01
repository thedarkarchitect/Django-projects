from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = '__all__' #all the fields in the Irder model
        fields = ['product', 'status']


