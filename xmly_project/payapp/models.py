from django.db import models

from shop_mall.models import Goods
from user.models import XMLYUser

ORDER_STATE_NO_PAY=1
ORDER_STATE_NO_SEND=2



class Orders(models.Model):
    o_user=models.ForeignKey(XMLYUser,on_delete=models.CASCADE)
    o_price = models.FloatField()
    o_order_num = models.CharField(max_length=50)
    o_time = models.DateTimeField(auto_now=True)
    o_state = models.IntegerField(default=1)

    class Meta:
        db_table='xmly_orders'

class OrderDetail(models.Model):
    o_order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    o_goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    o_goods_num = models.IntegerField()


    class Meta:
        db_table='xmly_orderdetail'
