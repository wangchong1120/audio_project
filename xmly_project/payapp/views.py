import os
from datetime import datetime


from django.core.cache import cache
from django.http import JsonResponse
from django.views import View
from rest_framework import viewsets,mixins
from rest_framework.response import Response

from payapp.filters import OrdersFilter
from payapp.models import Orders, OrderDetail
from payapp.serializer import OrderSerializer
from shop_car.models import Cart
from user.models import XMLYUser
from user.user_authentication import UserTokenAuthentication
from util.errors import XMLYException
from alipay import AliPay
#修改
from xmly_project import settings


class OrderViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.ListModelMixin):

    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (UserTokenAuthentication,)
    filter_class = OrdersFilter

    def get_queryset(self):
        return self.queryset.filter(o_user=self.request.user)

    def create(self, request, *args, **kwargs):

        carts = Cart.objects.filter(c_user=request.user,c_is_selected=True)

        if carts:
            total = 0
            for c in carts:
                total += c.c_goods.g_price * c.c_goods_num
            total = '{:.2f}'.format(total)

            o_order_num =datetime.now().strftime('%Y%m%d%H%M%S')+str(request.user.id)


            new_order = Orders.objects.create(o_user=request.user,o_price=float(total),o_order_num=o_order_num)

            ser = self.get_serializer(new_order)

            for c in carts:
                # 创建订单详情，并删除记录
                OrderDetail.objects.create(o_order=new_order, o_goods=c.c_goods, o_goods_num=c.c_goods_num)
                c.delete()
            result = {
                'order': ser.data
            }
            return Response(result)
        raise XMLYException({'code':609,'msg':'未选中商品，不能下单'})

class OrderPayView(View):


    def post(self, request):


        try:
            token = request.POST.get("token") if request.POST.get("token") else request.GET.get("token")
            user_id = cache.get(token)

            user = XMLYUser.objects.get(pk=user_id)
        except:
            raise XMLYException({"code": 610, "msg": "未登录，请先登录！！！"})

        o_order_number = request.POST.get("o_order_number")
        print('o_order_number=',o_order_number)
        if not o_order_number:
            raise XMLYException({"code": 611, "msg": "无效的订单号！"})
        try:
            order = Orders.objects.filter(o_user=user,o_order_num=o_order_number,o_state=1).first()
        except Orders.DoesNotExist:
            raise XMLYException({"code": 612, "msg": "订单错误！"})

        if order.o_price == 0:
            order.o_state = 2
            order.save()
            result = {
                'data': '支付成功'
            }
            return Response(result)

        # 业务处理:使用python sdk调用支付宝的支付接口
        # 初始化
        alipay = AliPay(
            appid="2016100200646279",  # 应用id
            app_notify_url=None,  # 默认回调url
            app_private_key_path=os.path.join(settings.BASE_DIR, 'payapp/keys/app_public_key.pem'),
            alipay_public_key_path=os.path.join(settings.BASE_DIR, 'payapp/keys/alipay_public_key.pem'),
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True  # 默认False
        )

        # 调用支付接口
        # 电脑网站支付，需要跳转到https://openapi.alipaydev.com/gateway.do? + order_string
        total_pay = order.o_price  # Decimal
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=o_order_number,  # 订单id
            total_amount=str(total_pay),  # 支付总金额
            subject='喜马拉雅商城%s' % o_order_number,
            return_url=None,
            notify_url=None  # 可选, 不填则使用默认notify url
        )
        # 返回应答
        pay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
        result = {
            "code": 200,
            "msg": "ok",
            'pay_url': pay_url
        }
        return JsonResponse(result)


class CheckPayView(View):
    # 查看订单支付的结果
    def post(self, request):
        # 用户是否登录
        try:
            token = request.POST.get("token") if request.POST.get("token") else request.GET.get("token")
            user_id = cache.get(token)
            user = XMLYUser.objects.get(pk=user_id)
        except:
            raise XMLYException({"code": 610, "msg": "未登录，请先登录！！！"})

        # 接收参数
        o_order_number = request.POST.get('o_order_number')
        # 校验参数
        if not o_order_number:
            raise XMLYException({"code": 611, "msg": "无效的订单号！"})
        try:
            order = Orders.objects.filter(o_user=user,o_order_num=o_order_number,o_state=1).first()
        except Orders.DoesNotExist:
            raise XMLYException({"code": 612, "msg": "订单错误！"})

        if order.o_state == 2:
            result = {
                'data': '已经支付！'
            }
            return Response(result)

        # 业务处理:使用python sdk调用支付宝的支付接口
        # 初始化
        alipay = AliPay(
            appid="2016100200646279",  # 应用id
            app_notify_url=None,  # 默认回调url
            app_private_key_path=os.path.join(settings.BASE_DIR, 'payapp/keys/app_public_key.pem'),
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
            alipay_public_key_path=os.path.join(settings.BASE_DIR, 'payapp/keys/alipay_public_key.pem'),

            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True  # 默认False
        )
        # 调用支付宝的交易查询接口
        while True:
            response = alipay.api_alipay_trade_query(o_order_number)
            code = response.get('code')
            if code == '10000' and response.get('trade_status') == 'TRADE_SUCCESS':
                # 支付成功
                # 获取支付宝交易号
                trade_no = response.get('trade_no')
                # 更新订单状态
                order.trade_no = trade_no
                order.o_state = 2
                order.save()
                # 返回结果
                result = {
                    "code": 200,
                    "msg": "ok",
                    'data': '支付成功'
                }
                return JsonResponse(result)
            elif code == '40004' or (code == '10000' and response.get('trade_status') == 'WAIT_BUYER_PAY'):
                # 等待买家付款
                # 业务处理失败，可能一会就会成功
                import time
                time.sleep(5)
                continue
            else:
                # 支付出错
                print(code)
                return JsonResponse({"code": 8003, "msg": "支付失败！"})


