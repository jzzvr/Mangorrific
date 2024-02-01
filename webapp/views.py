from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProductForm
from .models import Product
from .forms import ProductForm

def index(request):
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/about.html')

def menu(request):
    products = Product.objects.all()
    return render(request, 'webapp/menu.html', {'products': products})

def cart(request):
    return render(request, 'webapp/cart.html')

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')  # Add success message
            return redirect('menu')  # Redirect to menu page after editing
    else:
        form = ProductForm(instance=product)
    return render(request, 'webapp/edit_product.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('menu')  # Redirect to menu page after deletion
    return render(request, 'webapp/delete_product.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirect to menu page after adding
    else:
        form = ProductForm()
    return render(request, 'webapp/add_product.html', {'form': form})