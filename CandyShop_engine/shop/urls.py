from django.urls import path
from .views import CandyList

urlpatterns = [
    path('', CandyList.as_view(), name='candy_list_url')
]
