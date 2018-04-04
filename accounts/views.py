from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer, Stock, Cryptocurrency
from rest_framework import viewsets
from .serializers import CustomerSerializer, StockSerializer, CryptoSerializer
from .services import get_stock_price, get_crypto_price

def index(request):
    customer_list = Customer.objects.all()
    context = {'customer_list': customer_list}
    return render(request, 'accounts/index.html', context)

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}
    return render(request, 'accounts/customer_detail.html', context)

def stock_detail(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    stock.current_price = get_stock_price(stock.symbol)
    context = {'stock': stock}
    return render(request, 'accounts/stock_detail.html', context)

def crypto_detail(request, crypto_id):
    crypto = get_object_or_404(Cryptocurrency, pk=crypto_id)
    crypto.current_price = get_crypto_price(crypto.symbol)
    context = {'crypto': crypto}
    return render(request, 'accounts/crypto_detail.html', context)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptoSerializer