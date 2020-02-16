from django import forms


class AddToCartForm(forms.Form):
    count = forms.IntegerField(max_value=20)
