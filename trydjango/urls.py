"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from pages.views import home_view,contact_view,about_view
from blog.views import  article_create_view,article_detail_view,article_list_view
from login_user.views import login_view
urlpatterns = [
    path('products/',include('products.urls')), 
    #path('blog/',include('blog.urls')),
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('contact/',contact_view,name='contact'),
    path('about/<int:id>/',about_view,name='about'),
    path('blog/create/',article_create_view,name='article-create'),
    path('blog/<int:id>/',article_detail_view,name='article-detail'),
    path('blog/',article_list_view,name='article-list'),
    path("login/",login_view,name="login"),
    path('accounts/',include('django.contrib.auth.urls'))
]
