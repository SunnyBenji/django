import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .form import ProductForm
from .models import Product

# Create your views here.   
def index(request):
    try:
        products = Product.objects.all()
    except: 
        raise Http404("Aucun produit existant")
    return render(request, 'shop/index.html', locals())
def details(request, product_id ):
    try:
        product = Product.objects.get(pk=product_id)

    except Product.DoesNotExist:
        raise Http404("Ce produit n'existe pas")
    return render(request, 'shop/details.html', locals())
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
                product = Product()
                product.name = form.cleaned_data['name']
                product.description = form.cleaned_data['description']
                product.price = form.cleaned_data['price']
                product.quantity = form.cleaned_data['quantity']
                product.image = form.cleaned_data['image']

                product.save()
                return redirect('shop:all_product')
    else:
        form = ProductForm()
    
    return render(request, 'shop/create.html', locals())

def delete(request, product_id ):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Ce produit n'existe pas")
    if request.method == "POST":
        product.delete()
        return redirect('shop:all_product')
    return render(request, 'shop/delete.html', locals())