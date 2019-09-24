from django.shortcuts import render,get_object_or_404,redirect
from .forms import ProductForm,RawProductForm
# Create your views here.
from .models import Product

def product_create_view(request):
    form =ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    form= ProductForm()
    context={
        'form':form
    }
    return render(request,"products/product_create.html",context)

def render_initial_data(request):
    initial_data={
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=1)
    form =ProductForm(request.POST or None,instance=obj)#passing the object as instance
    if form.is_valid():
        form.save()
    context ={
         'form' : form
    }
    return render(request,"products/product_create.html",context)

def product_detail_view(request):

    obj=Product.objects.get(id=1)
    context={
        'object':obj
    }
    return render(request,"products/product_detail.html",context)

def dynamic_lookup_view(request,id):
    try:
        obj =Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context={
        'object': obj 
    }
    return render(request,"products/product_detail.html",context)

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

def product_list_view(request):
    queryset = Product.objects.all()#list of objects
    context ={
        "object_list" : queryset
    }
    return render(request,"products/product_list.html",context)