from django.shortcuts import render
from .forms import ProductForm,RawProductForm
# Create your views here.
from .models import Product

def render_initial_data(request):
    initial_data={
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=1)
    form =ProductForm(request.POST or None,instance=obj)#passing the object as instance
    if form.is_valid():
        form.save()
    context={
        'form': form
    }
    return render(request,"products/product_create.html",context)