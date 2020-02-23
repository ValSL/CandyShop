from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from django.core.mail import send_mail
from datetime import datetime


def time_limit_decorator(func):
    def wrapper(request):
        now_hour = datetime.now().hour + 3
        if now_hour >= 22 or now_hour <= 8:
            return render(request, 'orders/time_limit.html')
        else:
            return func(request)

    return wrapper


@time_limit_decorator
def order_create(request):
    cart = Cart(request)
    user = request.user
    if user.is_authenticated:
        try:
            buyer = request.user.buyer
        except:
            return render(request, 'orders/notbuyer.html')
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
