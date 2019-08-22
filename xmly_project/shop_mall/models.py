from django.db import models

class Goods(models.Model):
    g_name=models.CharField(max_length=100)
    g_img=models.CharField(max_length=200)
    g_price=models.FloatField()

    class Meta:
        db_table='goods'
