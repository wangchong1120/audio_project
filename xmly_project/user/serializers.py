import re

import redis
from django.contrib.auth.hashers import check_password
from rest_framework import serializers

from user.models import XMLYUser

#在序列化类中，可进行逻辑和格式验证
from util.errors import XMLYException

r=redis.Redis(host="localhost", port=6379, db=3)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=XMLYUser
        # fields=['id','u_username','u_password','u_telenumber','u_code']   #如果将id换做url，则需要导入mixins.RetrieveModelMixin,因为出现url代表要展示一条数据
        fields='__all__'  #表示序列化所有的字段



class UserLogin_contextSerializer(serializers.Serializer): #用来对注册的参数进行格式验证
    # 前后端商量好的参数名称
    p_num = serializers.CharField(max_length=11,required=True)
    #p_name = serializers.CharField(max_length=20)
    #password = serializers.CharField(max_length=256)  # 因为可能需要加密
    u_message = serializers.CharField(max_length=10)

    #格式验证完之后，需要进行逻辑验证
    def validate(self, attrs):
        u_telenumber=attrs.get('p_num')
        u_message=attrs.get('u_message')
        if not re.match(r'[1][3-9]\d{9}',u_telenumber):
            raise XMLYException({'code':6001,'msg':'手机号格式错误或手机号不存在,请重新输入!'})
        if not r.get(u_telenumber).decode():
            raise XMLYException({'code':6002,'msg':'验证码已过期,请重新发送!'})
        if r.get(u_telenumber).decode() != u_message:
            raise XMLYException({'code':6003,'msg':'验证码错误,请重新输入!'})
        return attrs




class UserLogin_pwdSerializer(serializers.Serializer): #用来对注册的参数进行格式验证
    # 前后端商量好的参数名称
    p_num = serializers.CharField(max_length=11,required=True)
    password = serializers.CharField(max_length=256)  # 因为可能需要加密

    #格式验证完之后，需要进行逻辑验证
    def validate(self, attrs):
        u_telenumber=attrs.get('p_num')
        password=attrs.get('password')
        if not re.match(r'[1][3-9]\d{9}',u_telenumber):
            raise XMLYException({'code':6005,'msg':'手机号格式错误或手机号不存在,请重新输入!'})
        user = XMLYUser.objects.filter(telenumber=attrs.get("p_num")).first()
        if not check_password(password, user.password):
            raise XMLYException({"code": 6006, "msg": "登录密码不正确!"})
        return attrs




class Set_PasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=10)

    def validate(self, attrs):
        password=attrs.get('password')
        if len(password) < 6:
            raise XMLYException({'code':6007,'msg':'密码至少需要六位数字'})
        return attrs




class Modify_PasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=10)  #表示当前密码
    new_password=serializers.CharField(max_length=10)
    again_password=serializers.CharField(max_length=10)

    def validate(self, attrs):
        # old_password=attrs.get('password')  #要和本地密码验证是否一样，可在视图集中实现
        new_password=attrs.get('new_password')
        again_password=attrs.get('again_password')
        if new_password != again_password:
            raise XMLYException({'code':6015,'msg':'密码不一致，修改密码失败！'})
        return attrs




class Modify_UsernameSerializer(serializers.Serializer):
    p_name=serializers.CharField(max_length=20)








