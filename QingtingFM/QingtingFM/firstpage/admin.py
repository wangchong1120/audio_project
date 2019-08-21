from django.contrib import admin

from firstpage.models import *
from personal.models import QTFMUser

@admin.register(Mainshow)       #注册指定模型，并与指定模型管理类关联
class MainshowAdmin(admin.ModelAdmin):  # 创建音频展示模型管理类
    list_display = ("id","title_id","title","img","loopnumber","setnumber")  #表中要展示的字段名
    list_per_page = 10      #设置每一页要显示的记录数
    ordering = ("id",)    #指定排序字段
    list_editable = ("title_id","title","img","loopnumber","setnumber")    #指定可以编辑的字段名
    search_fields = ("title_id","title")        #设置可以被搜索的字段
    list_filter = ("title",)            #设置可以被过滤的字段名

    def get_queryset(self, request):
        mainshow = super(admin.ModelAdmin,self).get_queryset(request)
        if request.user.is_superuser:       #判断当前发送请求的是否为超级用户
            return mainshow    #调研父类方法，返回所有模型
        else:
            return mainshow.filter(id__lte=10)    # 如果不是超级用户，只显示5条信息



@admin.register(Programlist)
class ProgramlistAdmin(admin.ModelAdmin):
    list_display = ("id","title_id", "title","program_name", "audio_id", "audio_href","loopnumber")  # 表中要展示的字段名
    list_per_page = 10  # 设置每一页要显示的记录数
    ordering = ("id","audio_id")  # 指定排序字段
    list_editable = ("title_id","title", "program_name","audio_id", "audio_href", "loopnumber")
    search_fields = ("title", "program_name","audio_id")
    list_filter = ("title",)

    def get_queryset(self, request):
        mainshow = super(admin.ModelAdmin,self).get_queryset(request)
        if request.user.is_superuser:       #判断当前发送请求的是否为超级用户
            return mainshow    #调研父类方法，返回所有模型
        else:
            return mainshow.filter(id__lte=10)    # 如果不是超级用户，只显示5条信息


@admin.register(QTFMUser)
class QTFMUserAdmin(admin.ModelAdmin):
    list_display = ("id","u_username", "u_telephone")
    list_per_page = 5
    ordering = ("id",)
    list_editable = ("u_username", "u_telephone")
    search_fields = ("u_username", "u_telephone")
    list_filter = ("u_username", "u_telephone")

    def get_queryset(self, request):
        mainshow = super(admin.ModelAdmin,self).get_queryset(request)
        if request.user.is_superuser:       #判断当前发送请求的是否为超级用户
            return mainshow    #调研父类方法，返回所有模型
        else:
            return mainshow.filter(id__lte=10)    # 如果不是超级用户，只显示5条信息