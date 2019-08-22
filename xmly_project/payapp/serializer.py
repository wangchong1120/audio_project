from rest_framework import serializers

from payapp.models import Orders, OrderDetail
from shop_mall.serializers import GoodsSerializer


class OrderSerializer(serializers.ModelSerializer):
    # #重写to_representation,将每一个订单转换为字典
    # def to_representation(self, instance):
    #     #继承父类to_representation，将对象拆分为字典
    #     order_dict=super().to_representation(instance)
    #     #获取订单详情的对象
    #     orderdetails=instance.orderdetail_set.all()
    #     #对订单详情进行序列化
    #     details = OrderDetailSerializer(orderdetails,many=True).data
    #     #给字典添加属性order_goods_info
    #     order_dict['order_goods_info']=details
    #     return order_dict

    class Meta:
        model = Orders
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):

    o_goods = GoodsSerializer()
    class Meta:
        model = OrderDetail
        fields = '__all__'


