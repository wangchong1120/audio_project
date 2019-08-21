from django.contrib import admin

# Register your models here.
from myapp.models import *



@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id","pro_name","pro_img","pro_intro","is_boy","is_good","is_vip")#显示字段
    list_per_page = 10 #设置每页设置10条记录
    ordering = ("id",)#指定排序字段
    list_editable = ("pro_name","pro_img","pro_intro")#可编辑字段
    search_fields = ("pro_name",)#可搜索字段
    list_filter = ("is_boy","is_good","is_vip")#过滤字段

    def get_queryset(self, request):
        pro = super(admin.ModelAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return pro
        else:
            return  pro.filter(id__lte=2)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","user_name", "password" )  # 显示字段
    list_per_page = 10  # 设置每页设置10条记录
    ordering = ("id",)  # 指定排序字段
    list_editable = ("user_name", "password")  # 可编辑字段
    search_fields = ("user_name",)  # 可搜索字段

    def get_queryset(self, request):
        user = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return user
        else:
            return user.filter(id__lte=2)


@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ("id","de_name", "de_img","mp4","de_info")  # 显示字段
    list_per_page = 10  # 设置每页设置10条记录
    ordering = ("id",)  # 指定排序字段
    list_editable = ("de_name","de_img","mp4","de_info")  # 可编辑字段
    search_fields = ("de_name","de_img","mp4","de_info")  # 可搜索字段


    def get_queryset(self, request):
        det = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return det
        else:
            return det.filter(id__lte=2)

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ("id","g_name","g_price","g_img")  # 显示字段
    list_per_page = 10  # 设置每页设置10条记录
    ordering = ("id",)  # 指定排序字段
    list_editable = ("g_name","g_price","g_img")  # 可编辑字段
    search_fields = ("g_name","g_price","g_img")  # 可搜索字段


    def get_queryset(self, request):
        goods = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return goods
        else:
            return goods.filter(id__lte=2)
