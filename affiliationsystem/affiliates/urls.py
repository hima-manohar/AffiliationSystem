

from django.urls import path
from .views import product_list, register_affiliate, record_sale

app_name = 'affiliates'

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('register/', register_affiliate, name='register_affiliate'),
    path('record-sale/<int:product_id>/', record_sale, name='record_sale'),
    
]
