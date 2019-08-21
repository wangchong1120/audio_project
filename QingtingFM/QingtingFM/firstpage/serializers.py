from rest_framework import serializers
from firstpage.models import *


class NavSerializer(serializers.ModelSerializer):   # 顶部导航序列化类
    class Meta:
        model = Nav
        fields = "__all__"                          # 模型中所有的属性


class WheelSerializer(serializers.ModelSerializer): # 轮播序列化类
    class Meta:
        model = Wheel
        fields = "__all__"


class MainshowSerializer(serializers.ModelSerializer):  # 页面主要展示序列化类
    class Meta:
        model = Mainshow
        fields = "__all__"


class ProgramlistSerializer(serializers.ModelSerializer):   # 音频章节目录序列化类
    class Meta:
        model = Programlist
        fields = "__all__"