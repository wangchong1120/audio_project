from django.db import models

from home_page.models import Details
from user.models import XMLYUser


class ListenSingle(models.Model):
    #关联XMLYUser（一对多，一个用户对应一条记录）
    l_user = models.ForeignKey(XMLYUser,on_delete=models.CASCADE)
    #关联Details（一对多，一个详情对应一条听单）
    l_details = models.ForeignKey(Details,on_delete=models.CASCADE)
    class Meta:
        db_table='listensingles'


class Download(models.Model):

    # 关联XMLYUser（一对多，一个用户对应一条记录）
    d_user = models.ForeignKey(XMLYUser,on_delete=models.CASCADE)
    # 关联Details（一对多，一个详情对应一条听单）
    d_details = models.ForeignKey(Details,on_delete=models.CASCADE)
    d_time = models.DateTimeField(auto_now=True) #下载时间
    class Meta:
        db_table='downloads'

