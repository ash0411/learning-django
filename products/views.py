from django.shortcuts import render

# Create your views here.
from .models import Product

def product_detail_view(request):
    obj=Product.objects.get(id=1)
    dontext={
        'object'=obj
    }
    return render(request, "product/detail.html",context)