from django.contrib import admin

from .models import Customer
from .models import Stock
from .models import Cryptocurrency

class StockInline(admin.StackedInline):
    model = Stock
    extra = 2

class CryptoInline(admin.StackedInline):
    model = Cryptocurrency
    extra = 2

class CustomerAdmin(admin.ModelAdmin):
    inlines = [StockInline, CryptoInline]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Stock)
admin.site.register(Cryptocurrency)