from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .forms import ProductForm,RawProductForm
# Create your views here.
from .models import Product

def dynamic_lookup_view(request,id):
    try:
        obj =Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context={
        'object': obj 
    }
    return render(request,"products/product_detail.html",context)