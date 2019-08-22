from django.db import models



#导航表
class Nav(models.Model):
    nav_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'navs'

#节目表
class Program(models.Model):
    pro_name=models.CharField(max_length=50)  #节目名称
    pro_img=models.CharField(max_length=200)  #图片地址
    pro_intro=models.CharField(max_length=256) #简介
    is_boy=models.BooleanField()  #是否是男生最爱
    is_good=models.BooleanField()  #是否是好听
    is_vip=models.BooleanField()  #是否是vip
    pro_type_id=models.IntegerField()  #类型   1：小说，2：儿童，3:70年，4：西安，5：other
                                    #00-99:类型名
    nav=models.ForeignKey(Nav,on_delete=models.CASCADE) #关联主要节目表

    class Meta:
        db_table='programs'

#详情表
class Details(models.Model):
    de_name=models.CharField(max_length=50)
    de_img=models.CharField(max_length=200)
    mp4=models.CharField(max_length=200)
    de_info=models.CharField(max_length=256)
    de_hits=models.IntegerField()  #点击量
    de_sub_num=models.IntegerField() #订阅量
    de_time=models.CharField(max_length=50)   #节目数据传入时间
    program=models.ForeignKey(Program,on_delete=models.CASCADE)  #关联节目表

    class Meta:
        db_table="details"

#轮播图
class Wheel(models.Model):
    w_img=models.CharField(max_length=200)  #轮播图图片地址
    program=models.OneToOneField(Program,on_delete=models.CASCADE)  #一对一关联节目表

    class Meta:
        db_table='wheels'


