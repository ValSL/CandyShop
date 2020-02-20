from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from django.core.mail import send_mail


def order_create(request):
    cart = Cart(request)
    user = request.user
    if user.is_authenticated:
        buyer = request.user.buyer
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
        if user.is_authenticated:
            form = OrderCreateForm(instance=user, initial={'phone_number': buyer.phone_number})
        else:
            form = OrderCreateForm()
        return render(request, 'orders/create.html', context={'form': form, 'cart': cart})
