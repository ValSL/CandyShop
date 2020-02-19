from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from django.core.mail import send_mail


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            cart.clear()
            send_mail(
                'Order in CandyShop',
                f'Your order number{order.id}',
                'ValSLTest@yandex.by',
                [order.email],
                fail_silently=False,
            )
            return render(request, 'orders/created.html', context={'order': order})
    else:
        form = OrderCreateForm()
        return render(request, 'orders/create.html', context={'form': form, 'cart': cart})
