from django.shortcuts import render,get_object_or_404
from .forms import ArticleModelForm
from .models import Article

# Create your views here.
def article_create_view(request):
    form = ArticleModelForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = ArticleModelForm()
    context -{
        form:"form"
    }
    return render(request,"blog/article_create.html",context)

def article_detail_view(request,id):

    obj= get_object_or_404(Article,id=id)
    context={
        'object':obj
    }
    return render(request,"blog/article_detail.html",context)

def article_list_view(request):
    queryset = Article.objects.all()#list of objects
    context ={
        "object_list" : queryset
    }
    return render(request,"blog/article_list.html",context)