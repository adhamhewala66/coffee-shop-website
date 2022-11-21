from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product
    
def search(request):
    return render(request, 'products/search.html')

def filter(request):
    products = Product.objects.all()
    name = None
    desc = None
    sfrom = None
    sto = None
    sensitive = None
    if 'sensitive' in request.GET:
        sensitive = request.GET['sensitive']
        if not sensitive:
            sensitive = 'off'
            
    if 'sname' in request.GET:
        name = request.GET['sname']
        if name:
            if sensitive == 'on':
                products = products.filter(name__contains=name)
            else:
                products = products.filter(name__icontains=name)
                
    if 'sdescription' in request.GET:
        desc = request.GET['sdescription']
        if desc:
            if sensitive == 'on':
                products = products.filter(desc__contains=desc)
            else:
                products = products.filter(desc__icontains=desc)
            
    if 'sfrom' in request.GET and 'sto' in request.GET:
        sfrom = request.GET['sfrom']
        sto = request.GET['sto']
        if sfrom and sto:
            if sfrom.isdigit() and sto.isdigit():
                products = products.filter(price__gte=sfrom, price__lte=sto)
    context={
        'products':products
    }
    return render(request, 'products/product_filter.html', context)
