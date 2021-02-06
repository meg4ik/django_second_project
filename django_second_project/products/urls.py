from django.urls import path

from .views import *


app_name = 'productsurl'
urlpatterns = [
    path('create/', product_create, name='create'),
    path('<int:eid>/', dynamic_lookup, name='product'),
    path('delete/<int:eid>/', product_delete, name='delete'),
    path('', product_list, name='list'),
    
]