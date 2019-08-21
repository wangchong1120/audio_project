from django.db import models



class Nav(models.Model):                          #顶部导航模型
    type_name = models.CharField(max_length=50)   #类型名称

    class Meta:
        db_table = "qtfm_nav"                     #数据库中表的名字


class Wheel(models.Model):                      #轮播模型
    img = models.CharField(max_length=250)      #图片的url
    title = models.CharField(max_length=256)    # 音频名称
    title_id = models.IntegerField()            # 音频对应的id
    type_name = models.CharField(max_length=50) #类型名称
    class Meta:
        db_table = "qtfm_wheel"


class Mainshow(models.Model):                       # mainshow模型
    img = models.CharField(max_length=250,verbose_name="图片的url")          # 图片的url
    type_name = models.CharField(max_length=50,verbose_name="类型名称")     # 类型名称
    type_child = models.CharField(max_length=20,verbose_name="子类型")    # 子类型
    title = models.CharField(max_length=256,verbose_name="音频节目名称")        # 音频节目名称
    title_id = models.IntegerField(verbose_name="音频节目对应的id")                # 音频节目对应的id
    text = models.CharField(max_length=100,verbose_name="展示简介")         # 展示简介
    text_detail = models.CharField(max_length=500,verbose_name="详细简介")  # 详细简介
    lector = models.CharField(max_length=20,verbose_name="分享人")        # 分享人
    lector_pic = models.CharField(max_length=256,verbose_name="分享人头像")   # 分享人头像
    loopnumber = models.CharField(max_length=20,verbose_name="总播放量")    # 总播放量
    setnumber = models.CharField(max_length=20,verbose_name="节目总期数")     # 节目总期数
    xiaoshuo_sex = models.CharField(max_length=5,verbose_name="小说类型男女分类")   # 小说类型男女分类
    typename_new = models.CharField(max_length=20,verbose_name="新人必听类型")  #新人必听类型

    def __str__(self):
        return self.title

    class Meta:
        db_table = "qtfm_mainshow"
        verbose_name = "音频展示模型"
        verbose_name_plural = verbose_name



class Programlist(models.Model):
    title = models.CharField(max_length=256,verbose_name="音频节目名称")        #音频节目名称
    title_id = models.IntegerField(verbose_name="音频节目对应的id")                #音频节目对应的id
    program_name = models.CharField(max_length=50,verbose_name="章节名称")  #章节名称
    audio_id = models.IntegerField(verbose_name="章节id")                #章节id
    audio_href = models.CharField(max_length=250,verbose_name="章节音频链接")   #章节音频链接
    duration = models.CharField(max_length=50,verbose_name="章节时长")      #章节时长
    loopnumber = models.CharField(max_length=50,verbose_name="章节播放量")    #章节播放量
    upload_time = models.CharField(max_length=50,verbose_name="章节上传时间")   #章节上传时间

    def __str__(self):
        name = self.title + self.program_name
        return name


    class Meta:
        db_table = "qtfm_programlist"
        verbose_name = "音频章节模型"
        verbose_name_plural = verbose_name




