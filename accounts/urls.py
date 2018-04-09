from django.conf.urls import url, include
#from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'stocks', views.StockViewSet)
router.register(r'cryptocurrency', views.CryptocurrencyViewSet)

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^customer/new/$', views.customer_new, name='customer_new'),
    url(r'^stock/new/$', views.stock_new, name='stock_new'),
    url(r'^crypto/new/$', views.crypto_new, name='crypto_new'),
    url(r'^(?P<customer_id>[0-9]+)/$', views.customer_detail, name='customer'),
    url(r'^(?P<customer_id>[0-9]+)/edit/$', views.customer_edit, name='customer_edit'),
    url(r'^(?P<customer_id>[0-9]+)/delete$', views.customer_delete, name='customer_delete'),
    url(r'^[0-9]+/stock/(?P<stock_id>[0-9]+)/$', views.stock_detail, name='stock'),
    url(r'^[0-9]+/stock/(?P<stock_id>[0-9]+)/edit/$', views.stock_edit, name='stock_edit'),
    url(r'^[0-9]+/stock/(?P<stock_id>[0-9]+)/delete/$', views.stock_delete, name='stock_delete'),
    url(r'^[0-9]+/crypto/(?P<crypto_id>[0-9]+)/$', views.crypto_detail, name='crypto'),
    url(r'^[0-9]+/crypto/(?P<crypto_id>[0-9]+)/edit/$', views.crypto_edit, name='crypto_edit'),
    url(r'^[0-9]+/crypto/(?P<crypto_id>[0-9]+)/delete/$', views.crypto_delete, name='crypto_delete'),
    url(r'^api/', include(router.urls)),
]