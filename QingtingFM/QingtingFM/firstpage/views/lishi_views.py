from rest_framework.decorators import api_view
from rest_framework.response import Response

from firstpage.serializers import *


@api_view(["GET"])
def lishi_view(request):
    wheels = Wheel.objects.filter(type_name="历史")
    mainshows_remen = Mainshow.objects.filter(type_name="历史",type_child="热门必听")
    mainshows_mingjia = Mainshow.objects.filter(type_name="历史",type_child="名家精选")
    mainshows_dangan = Mainshow.objects.filter(type_name="历史",type_child="档案秘闻")
    mainshows_fengyun = Mainshow.objects.filter(type_name="历史",type_child="风云人物")

    result = {
        'img_list': WheelSerializer(instance=wheels,many=True).data,
        'mainshows_remen' : MainshowSerializer(instance=mainshows_remen,many=True).data,
        'mainshows_mingjia' : MainshowSerializer(instance=mainshows_mingjia,many=True).data,
        'mainshows_dangan' : MainshowSerializer(instance=mainshows_dangan,many=True).data,
        'mainshows_fengyun': MainshowSerializer(instance=mainshows_fengyun, many=True).data,
        'type_child_list': ["热门必听","名家精选","档案秘闻","风云人物"]
    }
    return Response(result)