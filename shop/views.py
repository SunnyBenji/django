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

        form = ProductForm(request.POST)
        if form.is_valid():
            
            try:
                form.save()
                return redirect('shop:all_product')
            except:
                pass
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