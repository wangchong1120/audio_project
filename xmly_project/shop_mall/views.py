from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shop_mall.models import Goods
from shop_mall.serializers import GoodsSerializer


@api_view(['GET'])
def goods_view(request):
    goods=Goods.objects.all()
    print(goods)
    result = {
        'goods':GoodsSerializer(instance=goods,many=True).data
    }
    return Response(result)

