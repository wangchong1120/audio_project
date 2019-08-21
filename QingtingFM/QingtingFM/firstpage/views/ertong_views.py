from rest_framework.decorators import api_view
from rest_framework.response import Response

from firstpage.serializers import *


@api_view(["GET"])
def ertong_view(request):
    wheels = Wheel.objects.filter(type_name="儿童")
    mainshows_baobei = Mainshow.objects.filter(type_name="儿童", type_child="宝贝最爱")
    mainshows_tinggushi = Mainshow.objects.filter(type_name="儿童", type_child="听故事")
    mainshows_changerge = Mainshow.objects.filter(type_name="儿童", type_child="唱儿歌")
    mainshows_yuansheng = Mainshow.objects.filter(type_name="儿童", type_child="动画原声")

    result = {
        'img_list': WheelSerializer(instance=wheels, many=True).data,
        'ertong_baobei': MainshowSerializer(instance=mainshows_baobei, many=True).data,
        'ertong_tinggushi': MainshowSerializer(instance=mainshows_tinggushi, many=True).data,
        'ertong_changerge': MainshowSerializer(instance=mainshows_changerge, many=True).data,
        'ertong_yuansheng': MainshowSerializer(instance=mainshows_yuansheng, many=True).data,
        'type_child_list': ["宝贝最爱", "听故事","唱儿歌","动画原声"]

    }
    return Response(result)