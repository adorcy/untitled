from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer, Stock, Cryptocurrency
from rest_framework import viewsets
from .serializers import CustomerSerializer, StockSerializer, CryptoSerializer
from .services import get_stock_price, get_crypto_price
from .forms import CryptocurrencyForm, CustomerForm, StockForm
from django.shortcuts import redirect
from django.utils import timezone

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
    stock.original_value = stock.purchase_price * stock.number_of_shares
    stock.current_value = stock.current_price * stock.number_of_shares
    stock.profit = stock.current_value - stock.original_value
    context = {'stock': stock}
    return render(request, 'accounts/stock_detail.html', context)

def crypto_detail(request, crypto_id):
    crypto = get_object_or_404(Cryptocurrency, pk=crypto_id)
    crypto.current_price = get_crypto_price(crypto.symbol)
    crypto.original_value = crypto.purchase_price * crypto.number_of_coins
    crypto.current_value = crypto.current_price * crypto.number_of_coins
    crypto.profit = crypto.current_value - crypto.original_value
    context = {'crypto': crypto}

    def profit():
        profit=crypto.profit
        return profit

    return render(request, 'accounts/crypto_detail.html', context)

def crypto_edit(request, crypto_id):
    crypto = get_object_or_404(Cryptocurrency, pk = crypto_id)
    if request.method =="POST":
        form = CryptocurrencyForm(request.POST, instance=crypto)
        if form.is_valid():
            crypto = form.save(commit=False)
            crypto.modified = timezone.now()
            crypto.save()
            return redirect('crypto', crypto_id=crypto_id)
    else:
        form = CryptocurrencyForm(instance=crypto)
    return render(request, 'accounts/crypto_edit.html', {'form': form})

def stock_edit(request, stock_id):
    stock = get_object_or_404(Stock, pk = stock_id)
    if request.method =="POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.modified = timezone.now()
            stock.save()
            return redirect('stock', stock_id=stock_id)
    else:
        form = StockForm(instance=stock)
    return render(request, 'accounts/stock_edit.html', {'form': form})

def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, pk = customer_id)
    if request.method =="POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.modified = timezone.now()
            customer.save()
            return redirect('customer', customer_id=customer_id)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'accounts/customer_edit.html', {'form': form})

def customer_delete(request, customer_id):
    instance = Customer.objects.get(id=customer_id)
    instance.delete()
    return redirect('index')

def stock_delete(request, stock_id):
    instance = Stock.objects.get(id=stock_id)
    instance.delete()
    return redirect('customer', customer_id=instance.customer.id)

def crypto_delete(request, crypto_id):
    instance = Cryptocurrency.objects.get(id=crypto_id)
    instance.delete()
    return redirect('customer', customer_id=instance.customer.id)

def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created = timezone.now()
            customer.save()
            return redirect('customer', customer_id=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'accounts/customer_edit.html', {'form': form})

def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created = timezone.now()
            stock.date_purchased = timezone.now()
            stock.save()
            return redirect('stock', stock_id=stock.pk)
    else:
        form = StockForm()
    return render(request, 'accounts/stock_edit.html', {'form': form})

def crypto_new(request):
    if request.method == "POST":
        form = CryptocurrencyForm(request.POST)
        if form.is_valid():
            crypto = form.save(commit=False)
            crypto.created = timezone.now()
            crypto.date_purchased = timezone.now()
            crypto.save()
            return redirect('crypto', crypto_id=crypto.pk)
    else:
        form = CryptocurrencyForm()
    return render(request, 'accounts/stock_edit.html', {'form': form})

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptoSerializer