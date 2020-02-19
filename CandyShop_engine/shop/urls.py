from django.urls import path
from .views import (
    CandyList,
    CandyDetail,
    CurrentCandyList,
)

app_name = 'shop'
urlpatterns = [
    path('', CandyList.as_view(), name='candy_list_url'),
    path('<int:pk>/detail/', CandyDetail.as_view(), name='candy_detail_url'),
    path('candy/<int:pk>', CurrentCandyList.as_view(), name='current_candy_list_url'),
]
