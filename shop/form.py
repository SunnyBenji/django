from django import forms
from django.forms import Form
from .models import Product  

class ProductForm(forms.Form):  
    name = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()
    price =  forms.DecimalField()
    quantity = forms.IntegerField()