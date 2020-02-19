from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Candy
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Candy, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cart.add(product=product,
                 count=form.cleaned_data['count'],
                 update_count=form.cleaned_data['update'])

    return redirect('cart:cart_detail_url')


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Candy, id=id)
    cart.remove(product)
    return redirect('cart:cart_detail_url')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', context={'cart': cart})
