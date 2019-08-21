from rest_framework import serializers

from myapp.models import Nav, Program, Details, Wheel, Download, Listen, Goods, Car


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


class UserRegisterSerializer(serializers.Serializer):#用于注册验证的序列化类
    u_username = serializers.CharField(max_length=20,required=True)#对应前端手机号
    u_password = serializers.CharField(max_length=20,required=True)#对应手机号发送的验证码


class DownlodSerializer(serializers.Serializer):# 用户下载序列化类
    class Meta:
        model = Download
        fields = "__all__"


class LietenSerializer(serializers.Serializer):#用户听单对应序列化类
    class Meta:
        model = Listen
        fields = "__all__"

class GoodsSerializer(serializers.Serializer):#商品对应的序列化类
    class Meta:
        model = Goods
        fields = "__all__"

class CarSerializer(serializers.Serializer):#购物车序列化类
    class Meta:
        model = Car
        fields = "__all__"

