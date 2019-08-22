from rest_framework import serializers

from home_page.models import *


class ProSerializer(serializers.ModelSerializer):#节目表序列化类
    class Meta:
        model = Program
        fields = "__all__"

class NavSerializer(serializers.ModelSerializer): #导航栏序列化类
    #nav_name = ProSerializer()
    class Meta:
        model = Nav
        fields = "__all__"


class DetailsSerializer(serializers.ModelSerializer):#节目详情表序列化类
    class Meta:
        model = Details
        fields = "__all__"

class WheelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheel
        fields = "__all__"



