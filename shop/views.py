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
    imagePath = product.image.path
    
    return render(request, 'shop/details.html', locals())

def create(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:all_product')
            
    
    return render(request, 'shop/create.html', locals())

def edit(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Ce produits n'existe pas")
    
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            try:
                form.save()
                return redirect('shop:all_product')
            except:
                pass
    return render(request, 'shop/edit.html', locals())

def delete(request, product_id ):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Ce produit n'existe pas")
    if request.method == "POST":
        product.delete()
        return redirect('shop:all_product')
    return render(request, 'shop/delete.html', locals())