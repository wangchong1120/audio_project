from django.urls import path

from shop_mall.views import goods_view

urlpatterns = [
    path('all_goods/',goods_view),

]