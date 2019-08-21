from rest_framework.decorators import api_view
from rest_framework.response import Response

from firstpage.serializers import *


@api_view(["GET"])
def xsxp_view(request):
    wheels = Wheel.objects.filter(type_name="相声小品")
    mainshows_deyunshe = Mainshow.objects.filter(type_name="相声小品", type_child="德云社专区")
    mainshows_xiaopin = Mainshow.objects.filter(type_name="相声小品", type_child="小品荟萃")
    mainshows_dankou = Mainshow.objects.filter(type_name="相声小品", type_child="单口精品")
    mainshows_duikou = Mainshow.objects.filter(type_name="相声小品", type_child="对口精选")

    result = {
        'img_list': WheelSerializer(instance=wheels, many=True).data,
        'xsxp_deyunshe': MainshowSerializer(instance=mainshows_deyunshe, many=True).data,
        'xsxp_xiaopin': MainshowSerializer(instance=mainshows_xiaopin, many=True).data,
        'xsxp_dankou': MainshowSerializer(instance=mainshows_dankou, many=True).data,
        'xsxp_duikou': MainshowSerializer(instance=mainshows_duikou, many=True).data,
        'type_child_list': ["德云社专区", "小品荟萃", "单口精品","对口精选"]
    }
    return Response(result)