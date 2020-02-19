from django.urls import path
from .views import *

app_name = 'cart'
urlpatterns = [
    path('', cart_detail, name='cart_detail_url'),
    path('add/<int:id>', cart_add, name='cart_add_url'),
    path('remove/<int:id>', cart_remove, name='cart_remove_url'),
]
