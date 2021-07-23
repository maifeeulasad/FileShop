from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_description", "price"]


class ProductEmailForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["email"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        return super(LoginForm, self).clean(*args, **kwargs)