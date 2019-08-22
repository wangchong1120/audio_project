from django.db import models

# Create your models here.

class XMLYUser(models.Model):

    #"用户表"
    telenumber = models.CharField(max_length=11, unique=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=256) #因为可能需要加密


    class Meta:
        db_table="user"


class UserDetail(models.Model):
    u_user=models.ForeignKey(XMLYUser,on_delete=models.CASCADE)
    u_img=models.CharField(max_length=1024)
    u_wallet=models.FloatField(max_length=6)

    class Meta:
        db_table="user_detail"