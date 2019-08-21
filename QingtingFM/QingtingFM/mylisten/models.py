from django.db import models

from firstpage.models import Mainshow
from personal.models import QTFMUser

class MyDownload(models.Model):                                     #我的下载模型
    md_user = models.ForeignKey(QTFMUser,on_delete=models.CASCADE)  #关联用户模型
    md_radio = models.ForeignKey(Mainshow,on_delete=models.CASCADE) #关联mainshow模型

    class Meta:
        db_table = "qtfm_mydownload"


class MyCollection(models.Model):                                   #我的收藏模型
    mc_user = models.ForeignKey(QTFMUser,on_delete=models.CASCADE)  #关联用户模型
    mc_radio = models.ForeignKey(Mainshow,on_delete=models.CASCADE) #关mainshow模型

    class Meta:
        db_table = "qtfm_mycollextion"




class MyHistory(models.Model):                                      #我的历史模型
    mh_user = models.ForeignKey(QTFMUser,on_delete=models.CASCADE)  #关联用户模型
    mh_radio = models.ForeignKey(Mainshow,on_delete=models.CASCADE) #关mainshow模型

    class Meta:
        db_table = "qtfm_myhistory"


class MyBuy(models.Model):                                          #关联我的已购模型
    mb_user = models.ForeignKey(QTFMUser,on_delete=models.CASCADE)  #关联用户模型
    mb_radio = models.ForeignKey(Mainshow,on_delete=models.CASCADE) #关mainshow模型

    class  Meta:
        db_table = "qtfm_mybuy"