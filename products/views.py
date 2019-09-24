from django.shortcuts import render,get_object_or_404,redirect
from .forms import ProductForm,RawProductForm
# Create your views here.
from .models import Product

def product_delete_view(request,id):
    obj = get_object_or_404(Product,id=id)
    #POST request
    #obj.delete()
    if request.method == "POST":
        obj.delete()    #confirming delete
        return redirect('../../../about')
    context={
        'object': obj 
    }
    return render(request,"products/product_delete.html",context)