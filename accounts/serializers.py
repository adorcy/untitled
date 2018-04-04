from .models import Customer, Stock, Cryptocurrency
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'stock_set')


class StockSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='customer.name')
    class Meta:
        model = Stock
        fields = ('symbol', 'number_of_shares', 'owner')