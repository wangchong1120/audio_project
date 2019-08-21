from rest_framework import viewsets,mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from firstpage.serializers import *


@api_view(["GET"])
def tuijian_view(request):
    wheels = Wheel.objects.filter(type_name="推荐")
    mainshows_history = Mainshow.objects.filter(type_name="历史")[2::4]
    mainshows_pingshu = Mainshow.objects.filter(type_name="评书")[2::4]
    mainshows_xsxp = Mainshow.objects.filter(type_name="相声小品")[2::4]
    result = {
        'img_list': WheelSerializer(instance=wheels,many=True).data,
        'tuijian_history' : MainshowSerializer(instance=mainshows_history,many=True).data,
        'tuijian_pingshu' : MainshowSerializer(instance=mainshows_pingshu,many=True).data,
        'tuijian_xsxp' : MainshowSerializer(instance=mainshows_xsxp,many=True).data,
        'type_child_list': ["历史", "评书", "相声小品"]

    }
    return Response(result)     # 返回推荐页面渲染的数据









