from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, request=None, *args, **kwargs):
        self.user = request.user if request is not None else None
        super().__init__(*args, **kwargs)

    def set_form_fields(self):
        first_name = forms.CharField(max_length=100, initial=self.user.first_name, widget=forms.HiddenInput())
        last_name = forms.CharField(max_length=100, initial=self.user.last_name, widget=forms.HiddenInput())
        email = forms.EmailField(max_length=100, initial=self.user.email, widget=forms.HiddenInput())
        phone_number = forms.IntegerField(initial=self.user.id, widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),

        }
