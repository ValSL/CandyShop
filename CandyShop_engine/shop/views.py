from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Candy, CandyType, Cart
from .forms import AddToCartForm


def cart_add(request, pk):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        current_candy = Candy.objects.get(pk=pk)
        count = form['count'].data
        Cart.objects.create(candy=current_candy, count=count)
    return redirect('candy_list_url')


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


class CandyDetail(DetailView):
    model = Candy
    template_name = 'shop/candy_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddToCartForm()
        return context
