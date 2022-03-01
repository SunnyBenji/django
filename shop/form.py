from django import forms
from django.forms import ModelForm
from .models import Product  

class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom', 'title': 'Nom' }),
        }

        labels = {
            "name": "Nom",
            "price": "Prix",
            "quantity" : "Quantité"
        }
