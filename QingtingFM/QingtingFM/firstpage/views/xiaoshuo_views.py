from rest_framework.decorators import api_view
from rest_framework.response import Response

from firstpage.serializers import *


@api_view(["GET"])
def xiaoshuo_view(request):
    wheels = Wheel.objects.filter(type_name="小说")
    mainshows_xhcn = Mainshow.objects.filter(type_child="玄幻超能",xiaoshuo_sex="boy")
    mainshows_ffjx = Mainshow.objects.filter(type_child="付费精选",xiaoshuo_sex="boy")
    mainshows_lsmj = Mainshow.objects.filter(type_child="历史迷局",xiaoshuo_sex="boy")
    result = {
        'img_list': WheelSerializer(instance=wheels,many=True).data,
        'xiaoshuo_xhcn' : MainshowSerializer(instance=mainshows_xhcn,many=True).data,
        'xiaohuo_ffjx' : MainshowSerializer(instance=mainshows_ffjx,many=True).data,
        'xiaoshuo_lsmj' : MainshowSerializer(instance=mainshows_lsmj,many=True).data,
        'type_child_list' : ["玄幻超能","付费精选","历史迷局"]
    }
    return Response(result)


@api_view(["GET"])
def xiaoshuo_girl_view(request):
    wheels = Wheel.objects.filter(type_name="小说")[::-1]
    mainshows_xdyq = Mainshow.objects.filter(type_child="现代言情",xiaoshuo_sex="girl")
    mainshows_gdyq = Mainshow.objects.filter(type_child="古代言情",xiaoshuo_sex="girl")
    mainshows_pzxs = Mainshow.objects.filter(type_child="品质新书",xiaoshuo_sex="girl")
    mainshows_ffjx = Mainshow.objects.filter(type_child="付费精选",xiaoshuo_sex="girl")
    result = {
        'img_list': WheelSerializer(instance=wheels,many=True).data,
        'xiaoshuo_girl_xdyq' : MainshowSerializer(instance=mainshows_xdyq,many=True).data,
        'xiaoshuo_girl_gdyq' : MainshowSerializer(instance=mainshows_gdyq,many=True).data,
        'xiaoshuo_girl_pzxs' : MainshowSerializer(instance=mainshows_pzxs,many=True).data,
        'xiaoshuo_girl_ffjx': MainshowSerializer(instance=mainshows_ffjx, many=True).data,
        'type_child_list': ["现代言情", "古代言情", "品质新书","付费精选"]
    }
    return Response(result)


@api_view(["GET"])
def xiaoshuo_reting_view(request):
    wheels = Wheel.objects.filter(type_name="小说")
    mainshows_jinri = Mainshow.objects.filter(type_name="小说",xiaoshuo_sex="boy")[3:6]
    mainshows_all = Mainshow.objects.all()
    result = {
        'img_list' : WheelSerializer(instance=wheels,many=True).data,
        'xiaoshuo_jinri' : MainshowSerializer(instance=mainshows_jinri,many=True).data,
        'xiaoshuo_all' : MainshowSerializer(instance=mainshows_all,many=True).data,
        'type_child_list' : ["今日必听","全部"]
    }
    return Response(result)


@api_view(["GET"])
def xiaoshuo_changxiao_view(request):
    wheels = Wheel.objects.filter(type_name="小说")[::-1]
    mainshows_jinri = Mainshow.objects.filter(type_name="小说", xiaoshuo_sex="girl")[3:6]
    mainshows_all = Mainshow.objects.filter(type_name="小说", xiaoshuo_sex="girl")
    result = {
        'img_list' : WheelSerializer(instance=wheels,many=True).data,
        'xiaoshuo_jinri' : MainshowSerializer(instance=mainshows_jinri,many=True).data,
        'xiaoshuo_all' : MainshowSerializer(instance=mainshows_all,many=True).data,
        'type_child_list': ["今日必听", "全部"]

    }
    return Response(result)
