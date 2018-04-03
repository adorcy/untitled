from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer, Stock, Cryptocurrency

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
    context = {'stock': stock}
    return render(request, 'accounts/stock_detail.html', context)

def crypto_detail(request, crypto_id):
    crypto = get_object_or_404(Cryptocurrency, pk=crypto_id)
    context = {'crypto': crypto}
    return render(request, 'accounts/crypto_detail.html', context)
