from django.shortcuts import render
from .forms import ProductForm,RawProductForm
# Create your views here.
from .models import Product

def dynamic_lookup_view(request,id):
    obj = Product.objects.get(id=id)
    context={
        'object': obj 
    }
    return render(request,"products/product_detail.html",context)