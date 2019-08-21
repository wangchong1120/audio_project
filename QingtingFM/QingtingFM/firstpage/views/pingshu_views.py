from rest_framework.decorators import api_view
from rest_framework.response import Response

from firstpage.serializers import *


@api_view(["GET"])
def pingshu_view(request):
    wheels = Wheel.objects.filter(type_name="评书")
    mainshows_xiaobian = Mainshow.objects.filter(type_name="评书",type_child="小编力荐")
    mainshows_dantianfang = Mainshow.objects.filter(type_name="评书",type_child="单田芳评书")
    mainshows_liulanfang = Mainshow.objects.filter(type_name="评书",type_child="刘兰芳评书")
    mainshows_yuankuocheng = Mainshow.objects.filter(type_name="评书",type_child="袁阔成评书")

    result = {
        'img_list': WheelSerializer(instance=wheels,many=True).data,
        'pingshu_xiaobian' : MainshowSerializer(instance=mainshows_xiaobian,many=True).data,
        'pingshu_dantianfang' : MainshowSerializer(instance=mainshows_dantianfang,many=True).data,
        'pingshu_liulanfang' : MainshowSerializer(instance=mainshows_liulanfang,many=True).data,
        'pingshu_yuankuocheng': MainshowSerializer(instance=mainshows_yuankuocheng, many=True).data,
        'type_child_list': ["小编力荐", "单田芳评书", "刘兰芳评书", "袁阔成评书"]
    }
    return Response(result)