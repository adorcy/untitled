from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<customer_id>[0-9]+)/$', views.customer_detail, name='customer'),
    url(r'^[0-9]+/stock/(?P<stock_id>[0-9]+)/$', views.stock_detail, name='stock'),
    url(r'^[0-9]+/crypto/(?P<crypto_id>[0-9]+)/$', views.crypto_detail, name='crypto')
]