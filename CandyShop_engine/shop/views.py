from django.shortcuts import render
from django.views.generic import ListView
from .models import Candy, CandyType


class CandyList(ListView):
    model = Candy
    template_name = 'shop/index.html'
    context_object_name = 'candys'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        candys = Candy.objects.all()
        types = []
        for candy in candys:
            types.append(candy.type.title)
        types = set(types)
        context['types'] = types
        return context

