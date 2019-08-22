from django.shortcuts import render
from rest_framework import viewsets,mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response

from shop_car.models import Cart
from shop_car.serializers import CartSerializer
from user.user_authentication import UserTokenAuthentication
from util.errors import XMLYException


class  CartViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (UserTokenAuthentication,)
    #商品总价
    def total_price(self,user):
        carts = Cart.objects.filter(c_user = user,c_is_selected= True)
        total = 0
        for c in carts:
            total += c.c_goods.g_price * c.c_goods_num
        return '{:.2f}'.format(total)
    #购物车商品展示
    def list(self,request,*args,**kwargs):
        carts = Cart.objects.filter(c_user = request.user)
        ser = self.get_serializer(carts,many=True)
        result = {
            'carts':ser.data,
            'total_price':self.total_price(request.user)
        }
        return Response(result)
    #更新购物车中商品状态
    @list_route(methods=['POST'])
    def update_cart(self, request, *args, **kwargs):
        goodsid = request.data.get('goodsid')
        carts = Cart.objects.filter(c_user=request.user, c_goods_id=goodsid).first()
        carts.c_is_selected = not carts.c_is_selected
        carts.save()
        result = {
            'cart_id':carts.id,
            'total_price':self.total_price(request.user)
        }
        return Response(result)
    #更改所有购物车记录
    @list_route(methods=["PUT", "PATCH"])
    def updateall(self, request):
        carts = Cart.objects.filter(c_user=request.user)  # 获取当前用户的所有购物车记录
        for c in carts:
            c.c_is_selected = True
            c.save()

        result = {
            "update_success": "购物车状态已为全选",
            "total_price": self.total_price(request.user)
        }
        return Response(result)
    #添加商品
    @list_route(methods=['POST'])
    def add_cart(self,request):
        goodsid = request.data.get('goodsid')
        cart = Cart.objects.filter(c_user=request.user,c_goods_id=goodsid).first()
        current_cart_num = 1
        if cart:
            cart.c_goods_num += 1
            cart.save()
            current_cart_num = cart.c_goods_num
        else:
            try:
                Cart.objects.create(c_user = request.user,c_goods_id=goodsid)
            except:
                raise XMLYException({'code':601,'msg':'添加购物车失败!'})

        result = {
            'cart_num':current_cart_num
        }
        return Response(result)

    @list_route(methods=['POST'])
    def sub_cart(self,request):
        goodsid = request.data.get('goodsid')
        cart = Cart.objects.filter(c_user=request.user,c_goods_id=goodsid).first()
        current_cart_num = 0
        print('cart=',cart)
        if cart:
            if cart.c_goods_num > 1:
                cart.c_goods_num -= 1
                cart.save()
                current_cart_num = cart.c_goods_num
            else:
                cart.delete()

            result = {
                'cart_num':current_cart_num
            }
            return Response(result)
        else:
            raise XMLYException({'code':602,'msg':'购物车中无此商品，不能减去'})



