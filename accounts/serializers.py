from .models import Customer, Stock, Cryptocurrency
#from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone', 'street', 'city', 'state', 'zip', 'stock_set', 'cryptocurrency_set')


class StockSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='customer.name')
    class Meta:
        model = Stock
        fields = ('name', 'symbol', 'purchase_price', 'number_of_shares', 'owner', 'date_purchased')

class CryptoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='customer.name')
    class Meta:
        model = Cryptocurrency
        fields = ('name', 'symbol', 'purchase_price', 'number_of_coins', 'owner', 'date_purchased')