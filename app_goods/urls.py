from django.urls import path
from app_goods.views import items_list
from app_goods.views import update_prices



urlpatterns = [
    path('items/', items_list, name='item_list'),
    path('update_prices', update_prices, name='update_prices'),

    ]