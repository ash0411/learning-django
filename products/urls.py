from django.urls import path
from products.views import (
    product_create_view,
    render_initial_data,
    product_detail_view,
    dynamic_lookup_view,
    product_delete_view,
    product_update_view,
    product_list_view,
    )
app_name = "products"
urlpatterns =[
    path('<int:id>/',product_detail_view,name='product-detail'),
    path('create/',product_create_view,name='product-create'),
    path('initial/',render_initial_data,name='product-initial'),
    path('<int:id>/delete',product_delete_view,name='product-delete'),
    path('<int:id>/dynamic',dynamic_lookup_view,name='product'),
    path('',product_list_view,name='product-list'),
    path('<int:id>/update/',product_update_view, name='product-update'),
    ]