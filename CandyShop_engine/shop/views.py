from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Candy, CandyType
from django.contrib.auth.models import User
from cart.forms import CartAddProductForm


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


class CurrentCandyList(ListView):
    model = Candy
    template_name = 'shop/current_candy_list.html'
    context_object_name = 'candys'

    def get_queryset(self):
        candy_type = get_object_or_404(CandyType, pk=self.kwargs.get('pk'))
        return Candy.objects.filter(type=candy_type)


class CandyDetail(DetailView):
    model = Candy
    template_name = 'shop/candy_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartAddProductForm()
        return context
