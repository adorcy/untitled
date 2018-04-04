from django.db import models
from django.utils import timezone


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=30)
    name = models.TextField()
    number_of_shares = models.FloatField()
    purchase_price = models.FloatField()
    date_purchased = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}: {}".format(self.customer.name, self.symbol)

class Cryptocurrency(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=30)
    name = models.TextField()
    number_of_coins = models.FloatField()
    purchase_price = models.FloatField()
    date_purchased = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}: {}".format(self.customer.name, self.symbol)