from django import forms

from .models import Customer
from .models import Stock
from .models import Cryptocurrency

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'street', 'city', 'state', 'zip', 'email', 'phone')

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('customer','symbol', 'name', 'number_of_shares', 'purchase_price', 'date_purchased')

class CryptocurrencyForm(forms.ModelForm):

    class Meta:
        model = Cryptocurrency
        fields = ('customer', 'symbol', 'name', 'number_of_coins', 'purchase_price', 'date_purchased')