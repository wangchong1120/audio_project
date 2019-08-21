from django.db import models


class QTFMUser(models.Model):                                   #用户模型
    u_username = models.CharField(max_length=20,unique=True,verbose_name="用户昵称")    #用户昵称
    u_telephone = models.CharField(max_length=20,unique=True,verbose_name="用户电话")   #用户电话号码

    def __str__(self):
        return self.u_username

    class Meta:
        db_table = "qtfm_user"
        verbose_name = "用户模型"
        verbose_name_plural = verbose_name
