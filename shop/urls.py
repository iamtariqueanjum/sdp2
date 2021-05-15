from django.urls import path
from .views import *

urlpatterns = [
    path('', render_shop, name="shop-home"),
    path('sell', SellCreateView.as_view(), name="shop-sell"),
    path('buy', render_buy, name="shop-buy"),
    path('exchange',  ExchangeCreateView.as_view(), name="shop-exchange"),

    path('load-models/', load_models, name='load_models'),
    path('load-variants/', load_variants, name='load_variants'),

]