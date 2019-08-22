from django.db import models

from shop_mall.models import Goods
from user.models import XMLYUser


class Cart(models.Model):
    #关联用户表
    c_user=models.ForeignKey(XMLYUser,on_delete=models.CASCADE)
    c_goods=models.ForeignKey(Goods,on_delete=models.CASCADE)
    c_goods_num=models.IntegerField(default=1)
    c_is_selected=models.BooleanField(default=True)
    class Meta:
        db_table='carts'

