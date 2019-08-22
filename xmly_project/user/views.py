import uuid

import redis
from django.contrib.auth.hashers import make_password
from django.core.cache import cache

from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response

from user.models import XMLYUser
import http.client
import random

import urllib

from user.serializers import UserSerializer, UserLogin_contextSerializer, Set_PasswordSerializer, \
    UserLogin_pwdSerializer, Modify_PasswordSerializer, Modify_UsernameSerializer
from util.errors import XMLYException

r=redis.Redis(host="localhost", port=6379, db=3)  #redis密码已经取消

class UserViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,
                  mixins.CreateModelMixin):

    queryset = XMLYUser.objects.all()
    serializer_class = UserSerializer   #因为序列化绑定了模型


    #接口一    将前端键入的数据通过  API接口{键入数据}  格式给后端
    #手机验证码登录
    @list_route(methods=['GET','POST'],serializer_class=UserLogin_contextSerializer)         #可以将下边的函数名称作为API接口的最后一部分
    def Login_message(self,request):     #request表示前端发来的请求

        if request.method=='GET':  #在此需要获取短信验证的短信验证码
            mobile=request.GET.get('p_num')
            # mobile=request.query_params.get('p_num')
            print(mobile)
            host = "106.ihuyi.com"
            sms_send_uri = "/webservice/sms.php?method=Submit"

            # 用户名是登录用户中心->验证码短信->产品总览->APIID
            account = "C93921996"
            # 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
            password = "03619bfcd21b1ad29bd3bb5e75e20ef7"
            u_message = random.randint(100000, 999999)
            text = "您的验证码是：" + str(u_message) + "。请不要把验证码泄露给其他人。"  # 格式不能随便改动
            print('@@@@@@@@@@@@@@@@@@@@@@')
            print(text)
            params = urllib.parse.urlencode(
                {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
            conn = http.client.HTTPConnection(host, port=80, timeout=30)
            conn.request("POST", sms_send_uri, params, headers)
            r.set(mobile,u_message,ex=60*60*24)  #将短信验证码存储在Redis中，过期时间设置为180秒
            conn.close()
            result={
                'msg':"短信发送成功",
            }
            return Response(result)


        if request.method=='POST':
            print('进入POST执行~~~')
            serializer = self.get_serializer(data=request.data)
            is_valid=serializer.is_valid(raise_exception=False)  #返回值为false或ture,False可以精确制导报错在哪
            if not is_valid:  #若格式验证没有成功
                raise XMLYException({'code':6000,'msg':'数据格式错误,登陆失败~~~'})
            #如果验证成功，则走接下来的步骤
            u_telenumber=serializer.data['p_num']
            # u_message=serializer.data['u_message']
            if not XMLYUser.objects.filter(telenumber=u_telenumber).exists():
                new_user=XMLYUser.objects.create(telenumber=u_telenumber)
            else:
                new_user = XMLYUser.objects.filter(telenumber=u_telenumber).first()
            #登录或创建成功，就可以删除redis中的mobile验证码
            r.delete(u_telenumber)
            token = uuid.uuid4().hex  # 随机生成token字符串
            cache.set(token, new_user.id, timeout=60 * 60 * 24)  #服务端存储token
            result={
                'user_id':new_user.id,                          #发送给前端的token
                'token':token
            }
            return Response(result)

    # 手机密码登录
    @list_route(methods=['POST'], serializer_class=UserLogin_pwdSerializer)  # 可以将下边的函数名称作为API接口的最后一部分
    def Login_pwd(self, request):  # request表示前端发来的请求
        serializer = self.get_serializer(data=request.data)
        is_valid = serializer.is_valid(raise_exception=False)
        if not is_valid:
            raise XMLYException({'code': 6004, 'msg': '数据格式错误,登陆失败~~~'})
        user = XMLYUser.objects.filter(telenumber=serializer.data['p_num']).first()
        token = uuid.uuid4().hex  # 随机生成token字符串
        cache.set(token, user.id, timeout=60 * 60 * 24)
        result = {
            'user_id': user.id,
            'token': token
        }
        return Response(result)


    #设置密码

    @list_route(methods=['POST',],serializer_class=Set_PasswordSerializer)  #需要让前端发送一个token来判断是否登录，若没有登陆返回登录页面
    def Set_Pwd(self,request):

        if request.method=='POST':  #前端输入要设置的密码后进行如下操作
            token=request.data.get('token')
            user_id=cache.get(token)
            user=XMLYUser.objects.filter(id=user_id).first()
            if not user:
                raise XMLYException({'code':6008,'msg':'用户未登录，请先登录!'})
            serializer = self.get_serializer(data=request.data)
            is_valid=serializer.is_valid(raise_exception=False)
            if not is_valid:
                raise XMLYException({'code':6009,'msg':'设置密码失败！'})
            #如果设置密码成功
            password=serializer.data['password']
            u_password=make_password(password)
            user.password=u_password #将密码已加密的形式存入数据库
            user.save()
            result={
                'code':6010,
                'msg':'设置密码成功!'
            }
            return Response(result)

    #修改密码

    @list_route(methods=['POST', ], serializer_class=Modify_PasswordSerializer)  # 需要让前端发送一个token来判断是否登录，若没有登陆返回登录页面
    def Modify_Pwd(self, request):

        if request.method == 'POST':  # 前端输入要设置的密码后进行如下操作
            token = request.data.get('token')
            user_id = cache.get(token)
            user = XMLYUser.objects.filter(id=user_id).first()
            if not user:
                raise XMLYException({'code': 6011, 'msg': '用户未登录，请先登录!'})
            serializer = self.get_serializer(data=request.data)

            is_valid = serializer.is_valid(raise_exception=False)
            if not is_valid:
                raise XMLYException({'code': 6013, 'msg': '修改密码失败！'})
            # old_password = serializer.data['password']
            # if old_password != user.password:
            #     raise XMLYException({'code': 6012, 'msg': '旧密码输入错误！'})
            # 如果设置密码成功
            password = serializer.data['new_password']
            u_password = make_password(password)
            user.password = u_password  # 将密码已加密的形式存入数据库
            user.save()
            result = {
                'code': 6014,
                'msg': '修改密码成功!'
            }
            return Response(result)

    #修改用户名称

    @list_route(methods=['POST', ], serializer_class=Modify_UsernameSerializer)  # 需要让前端发送一个token来判断是否登录，若没有登陆返回登录页面
    def Modify_Username(self, request):

        if request.method == 'POST':  # 前端输入要设置的密码后进行如下操作
            token = request.data.get('token')
            user_id = cache.get(token)
            user = XMLYUser.objects.filter(id=user_id).first()
            if not user:
                raise XMLYException({'code': 6016, 'msg': '用户未登录，请先登录!'})
            serializer = self.get_serializer(data=request.data)
            is_valid = serializer.is_valid(raise_exception=False)
            if not is_valid:
                raise XMLYException({'code': 6017, 'msg': '修改用户名失败！'})
            # 如果设置密码成功
            username = serializer.data['p_name']
            user.username=username
            user.save()
            result = {
                'code': 6018,
                'msg': '修改用户名成功!'
            }
            return Response(result)




