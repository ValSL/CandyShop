from django.shortcuts import render, redirect
from .forms import UserRegisterForm, BuyerRegisterForm
from django.contrib import messages
from .models import Buyer


def register(request):
    if request.method == 'POST':
        form_u = UserRegisterForm(request.POST)
        form_b = BuyerRegisterForm(request.POST)
        if form_b.is_valid() and form_u.is_valid():
            user = form_u.save()
            buyer = Buyer.objects.create(user=user, phone_number=form_b.cleaned_data.get('phone_number'))
            username = form_u.cleaned_data['username']
            messages.success(request, f'Account created for {username}')
            return redirect('login_url')
    else:
        form_u = UserRegisterForm()
        form_b = BuyerRegisterForm()
        return render(request, 'users/register.html', context={'form_u': form_u, 'form_b': form_b})
