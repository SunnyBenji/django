from django import forms
from django.forms import ModelForm
from .models import Product  

class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }