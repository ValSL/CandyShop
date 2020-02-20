from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from django.core.mail import send_mail


def order_create(request):
    cart = Cart(request)
    user = request.user
    if request.method == 'POST':
        if user.is_authenticated:
            form = OrderCreateForm(request, request.POST)
            form.set_form_fields()
        else:
            form = OrderCreateForm(request, request.POST)

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
