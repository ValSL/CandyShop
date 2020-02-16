from django.urls import path
from .views import (
    CandyList,
    CandyDetail,
    cart_add,
)

urlpatterns = [
    path('', CandyList.as_view(), name='candy_list_url'),
    path('<int:pk>/detail/', CandyDetail.as_view(), name='candy_detail_url'),
    path('add-to-cart/<int:pk>', cart_add, name='cart_add_url'),
]
