from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1>HEllo world</h1>") #string of html code
    return render(request,"home.html",{})

def contact_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1>HEllo world</h1>") #string of html code
    return render(request,"contact.html",{})
def about_view(request,*args, **kwargs):
    my_context={
        "title":"thsi si about us",
        "this_is_true":True,
        "my_number":123,
        "my_list":[123,456,789,"Abc"],
        "my_html":"<h1>Hello world</h1>"

    }
    return render(request,"about.html",my_context)
def social_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return HttpResponse("<h1>Socail Page</h1>") #string of html code
    


