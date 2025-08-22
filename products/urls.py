from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu_items/',MenuItemListView.as_view(), name="menu_items"),
]