import random
from random import randint

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route, api_view
from rest_framework.response import Response

from myapp.models import *
from myapp.nav_serializer import NavSerializer, DetailsSerializer, ProSerializer


#主页展示接口
#主页导航栏：默认是推荐，1：小说，2：儿童，3：历史，4：70年
from util.errors import XMLYException


class MainShowSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,mixins.DestroyModelMixin):

    queryset = Nav.objects.all()#对应数据库 ，导航模型
    serializer_class = NavSerializer #关联导航栏序列化类

    #主页 推荐节目表
    @list_route(methods=["GET"],serializer_class=ProSerializer)#该装饰装饰的函数，名称作为路由的一部分
    def recommend(self,request):

        guess_like_list = []  #定义节目列表
        geuss_like_id = []#定义节目表id

        #获取9个节目表的id
        for temp in range(9):
            id = randint(1,132)
            geuss_like_id.append(id)

        #遍历id列表
        for temp in  geuss_like_id:
            pro_guess_like = Program.objects.get(id=temp)#从数据库查id对应的节目表
            ser_pro_guess = self.get_serializer(pro_guess_like)#将节目序列化
            guess_like_list.append(ser_pro_guess.data)#添加到节目列表中

        #组装节目信息
        result = {
            "data":guess_like_list
        }

        return Response(result)#将节目信息返回


    #推荐导航
    def list(self, request, *args, **kwargs):
        print("a"*100)
        nav_queryset = self.get_queryset() #从数据库查询导航集合
        ser_nav = self.get_serializer(nav_queryset)# 查询结果序列化


        type_list = []#定义子版块列表
        pro_list = nav_queryset.first().program_set.all()#通过导航栏id获取与他关联的下一级节目表1



    #导航，1：小说，2：儿童，3:70年，4：历史，
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()#获取导航单个实例
        except:
            raise XMLYException({"code":"5000","msg":"访问的页面不存在"})


        nav_queryset = self.get_queryset()#从数据库查询导航集合
        ser_nav = self.get_serializer(nav_queryset)#导航查询结果序列化


        #id:1 表示小说
        if instance.id == 1:
            #轮播图

            pic_list = []#定义存放轮播图片的列表
            wheel_pic_id = [1,2,3,4]# 小说的轮播图id
            for temp in wheel_pic_id:#遍历小说轮播图id列表
                wheel_pic = Wheel.objects.get(id=temp)#通过id查询数据库对应的轮播记录
                wheel_pic_dict = {
                    "program_id":wheel_pic.program_id,#轮播图对应的节目id
                    "wheel_pic":wheel_pic.w_img,#轮播图片
                }
                pic_list.append(wheel_pic_dict)#将轮播记录的图片路径存放到列表中

            #组装轮播图数据
            pic_wheel_result = {
                "wheel_pic":pic_list
            }



            #男生、女生最爱
            nav_queryset = self.get_queryset()#得到小说导航栏对应的集合
            fic_pro_id = nav_queryset.first().id#获取导航小说的id

            fic_queryset = Program.objects.filter(nav_id=fic_pro_id)#从节目表过滤出小说集合
            boy_fic_queryset = fic_queryset.filter(is_boy=0)#从小说集合过滤出男生集合
            girl_fic_queryset = fic_queryset.filter(is_boy=1)#从小说结合过滤出女生集合
            boy_pro_list = []#定义存储男生喜欢的节目信息
            girl_pro_list = []
            for temp in boy_fic_queryset:#遍历男生喜欢的小说集合
                #组装数据
                boy_one_dict = {
                    "pro_id":temp.id,
                    "pro_img":temp.pro_img,
                    "pro_name":temp.pro_name,
                    "pro_intro":temp.pro_intro
                }
                #将组装好的每个节目信息添加到列表中
                boy_pro_list.append(boy_one_dict)

            for temp in girl_fic_queryset:#遍历男生喜欢的小说集合
                #组装数据
                girl_one_dict = {
                    "pro_id": temp.id,
                    "pro_img":temp.pro_img,
                    "pro_name":temp.pro_name,
                    "pro_intro":temp.pro_intro
                }
                #将组装好的每个节目信息添加到列表中
                girl_pro_list.append(girl_one_dict)
            #组装男生小说结果数据
            boy_result = {
                "data":boy_pro_list
            }
            girl_result = {
                "data":girl_pro_list
            }

            # 暴爽劲听

            listen_fic_queryset = fic_queryset.filter(is_good=1)#从小说集合过滤出暴爽劲听集合
            listen_pro_list = []#定义存储暴爽劲听节目信息的列表
            for temp in listen_fic_queryset:#遍历暴爽劲听集合
                #组装每个节目需要的数据
                listen_one_dict = {
                    "pro_id": temp.id,
                    "pro_img": temp.pro_img,
                    "pro_name": temp.pro_name,
                    "pro_intro": temp.pro_intro
                }
                #组装好的数据添加到列表中
                listen_pro_list.append(listen_one_dict)

            #组装暴爽劲听数据结果
            listen_result = {
                "data":listen_pro_list
            }


           # vip专区
            vip_fic_queryset = fic_queryset.filter(is_vip=1)#从小说结合过滤出vip
            vip_pro_list = []#定义存储vip节目的列表
            for temp in vip_fic_queryset:#遍历vip节目集合
                #组装单个vip节目信息的数据
                vip_one_dict = {
                    "pro_id": temp.id,
                    "pro_img": temp.pro_img,
                    "pro_name": temp.pro_name,
                    "pro_intro": temp.pro_intro
                }
                #将单个节目信息添加到列表中
                vip_pro_list.append(vip_one_dict)
            #组装vip节目数据
            vip_result = {
                "data":vip_pro_list
            }

            #推荐
            rec_pro_list = []#定义存储推荐节目的列表
            for temp in range(3):#默认给3个节目
                rec_one = random.choice(fic_queryset)#每次从小说集合随机挑选一个节目
                #从随机挑选的这个节目中拆分每一个推荐节目需要的字段进行组装
                rec_one_dict = {
                    "pro_id": rec_one.id,#节目id
                    "pro_img":rec_one.pro_img,#图片路径
                    "pro_name":rec_one.pro_name,#节目名称
                    "pro_intro":rec_one.pro_intro#节目介绍
                }
                #将每个节目添加到推荐列表中
                rec_pro_list.append(rec_one_dict)
            #组装推荐结果
            rec_result = {
                "data":rec_pro_list
            }

            fic_result = {
                "pic_wheel_result":pic_wheel_result,#轮播图
                "boy_result":boy_result,#男生喜欢
                "girl_result":girl_result,#女生喜欢
                "vip_result":vip_result,#vip专区
                "listen_result":listen_result,#暴爽劲听
                "rec_result":rec_result#推荐
            }
            return Response(fic_result)#将小说页面数据返回


        elif instance.id == 2:
            #id:2 表示儿童
            #儿童轮播图
            pic_list = []  # 定义存放轮播图片的列表
            wheel_pic_id = [2, 3, 4, 5]  # 儿童的轮播图id
            for temp in wheel_pic_id:  # 遍历儿童轮播图id列表
                wheel_pic = Wheel.objects.get(id=temp)  # 通过id查询数据库对应的轮播记录
                wheel_pic_dict = {
                    "program_id":wheel_pic.program_id,
                    "wheel_pic":wheel_pic.w_img
                }
                pic_list.append(wheel_pic_dict)  # 将轮播记录的图片路径存放到列表中

            # 组装轮播图数据
            pic_wheel_result = {
                "wheel_pic": pic_list
            }

            child_pro_id = instance.id#获取导航儿童的id
            child_queryset = Program.objects.filter(nav_id=child_pro_id)

            #经典故事
            sto_pro_list = []  # 定义存储推荐节目的列表
            for temp in range(6):  # 默认给6个节目
                sto_one = random.choice(child_queryset)  # 每次从儿童集合随机挑选一个节目
                # 从随机挑选的这个节目中拆分每一个推荐节目需要的字段进行组装
                sto_one_dict = {
                    "pro_id":sto_one.id,
                    "pro_img": sto_one.pro_img,  # 图片路径
                    "pro_name": sto_one.pro_name,  # 节目名称
                    "pro_intro": sto_one.pro_intro  # 节目介绍
                }
                # 将每个节目添加到推荐列表中
                sto_pro_list.append(sto_one_dict)
            # 组装推荐结果
            sto_result = {
                "data": sto_pro_list
            }

            #启智儿歌
            song_pro_list = []#定义启智儿歌节目存放列表
            song_pro_queryset = child_queryset.filter(is_good=0)#过滤儿歌节目集合

            for temp in song_pro_queryset:#遍历集合
                #拆分数据组装成单个节目
                song_one_dict = {
                    "pro_id":temp.id,#节目id
                    "pro_img": temp.pro_img,  # 图片路径
                    "pro_name": temp.pro_name,  # 节目名称
                    "pro_intro": temp.pro_intro  # 节目介绍
                }
                #将单个节目添加节目列表
                song_pro_list.append(song_one_dict)

            song_result = {
                "data":song_pro_list
            }

            child_result = {
                "pic_wheel_result":pic_wheel_result,
                "sto_result":sto_result,
                "song_result":song_result
            }
            return Response(child_result)
        elif instance.id == 4:
            #70年
            pic_list = []  # 定义存放轮播图片的列表
            wheel_pic_id = [3, 4, 5, 6]  # 儿童的轮播图id
            for temp in wheel_pic_id:  # 遍历70年轮播图id列表
                wheel_pic = Wheel.objects.get(id=temp)  # 通过id查询数据库对应的轮播记录
                wheel_pic_dict = {
                    "program_id":wheel_pic.program_id,
                    "wheel_pic":wheel_pic.w_img

                }
                pic_list.append(wheel_pic_dict)  # 将轮播记录的图片路径存放到列表中

            # 组装轮播图数据
            pic_wheel_result = {
                "wheel_pic": pic_list
            }


            year70_pro_id = instance.id
            year70_pro_queryset = Program.objects.filter(nav_id=year70_pro_id)

            # 时代强音
            voice_pro_queryset = year70_pro_queryset.filter(is_good=1)#从70年过滤时代强音

            voice_pro_list = []#定义时代强音节目列表
            for temp in voice_pro_queryset:#遍历时代强音集合
                #拆分数据
                vioce_one_dict = {
                    "pro_id":temp.id,
                    "pro_img": temp.pro_img,  # 图片路径
                    "pro_name": temp.pro_name,  # 节目名称
                    "pro_intro": temp.pro_intro  # 节目介绍
                }
                #添加到时代强音列表中
                voice_pro_list.append(vioce_one_dict)

            #组装时代强音数据
            voice_result = {
                "data":voice_pro_list
            }

            #中华美韵
            china_pro_queryset = year70_pro_queryset.filter(is_good=0)
            china_pro_list = []
            for temp in range(6):
                china_one_pro = random.choice(china_pro_queryset)
                china_one_dict = {
                    "pro_img":china_one_pro.pro_img,
                    "pro_name":china_one_pro.pro_name,
                    "pro_intro":china_one_pro.pro_intro
                }

                china_pro_list.append(china_one_dict)

            china_result = {
                "data":china_pro_list
            }

            year70_result = {
                "pic_wheel_result":pic_wheel_result,
                "voice_result":voice_result,
                "china_result":china_result
            }
            return Response(year70_result)
        elif instance.id == 3:

            #历史轮播图
            pic_list = []  # 定义存放轮播图片的列表
            wheel_pic_id = [12, 13, 14, 15]  # 儿童的轮播图id
            for temp in wheel_pic_id:  # 遍历70年轮播图id列表
                wheel_pic = Wheel.objects.get(id=temp)  # 通过id查询数据库对应的轮播记录
                wheel_pic_dict = {
                    "program_id":wheel_pic.program_id,
                    "wheel_pic":wheel_pic.w_img
                }
                pic_list.append(wheel_pic_dict)  # 将轮播记录的图片路径存放到列表中

            # 组装轮播图数据
            pic_wheel_result = {
                "wheel_pic": pic_list
            }

            #历史
            history_pro_id = instance.id
            history_pro_queryset = Program.objects.filter(nav_id=history_pro_id)#从节目表过滤出历史节目

            classic_pro_list = []#定义存储经典必听节目的列表
            for temp in range(6):#
                history_one_pro = random.choice(history_pro_queryset)#从历史节目中任意挑选6个作为经典必听节目
                #组装每个经典必听节目
                history_one_dict = {
                    "pro_id":history_one_pro.id,
                    "pro_img":history_one_pro.pro_img,
                    "pro_name":history_one_pro.pro_name,
                    "pro_intro":history_one_pro.pro_intro
                }
                #将每个节目添加到列表中
                classic_pro_list.append(history_one_dict)

            #组装经典必听数据
            classic_result = {
                "data":classic_pro_list
            }

            #组装历史页面数据
            history_result = {
                "pic_wheel_result": pic_wheel_result,
                "classic_result":classic_result
            }
            return Response(history_result)





#子版块

class ChildViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, mixins.DestroyModelMixin):

    queryset = Program.objects.all()#从节目表得到结合
    serializer_class = ProSerializer#将节目表序列化


    #小说子版块 参数：0：排行 1：言情 2：悬疑 3：都市 4：畅销书 5：幻想 6：历史
    @list_route(methods=["GET"])
    def fic_child(self,request):
        cla_list = ["排行榜","言情","悬疑","都市","畅销书","幻想","历史"]

        try:
            child_id = request.query_params["child_id"]
            test = cla_list[int(child_id)]
        except:
            raise XMLYException({"code":5000,"msg":"页面信息不存在！"})


        queryset = self.get_queryset()#得到所有节目的集合
        fic_queryset = queryset.filter(nav_id=1)#过滤出小说的节目

        pro_list = []#定义存储小说节目信息列表

        for temp in fic_queryset:
            kind = temp.pro_type_id % 10

            if int(request.query_params["child_id"]) == kind:
                #组装数据
                pro_one_dict = {
                    "id":temp.id,
                    "pro_img":temp.pro_img,
                    "pro_name":temp.pro_name,
                    "pro_intro":temp.pro_intro
                }
                pro_list.append(pro_one_dict)
        result = {
            "data":pro_list
        }

        return Response(result)


    #儿童子版块
    @list_route(methods=["GET"])
    def child_child(self, request):
        cla_list = ["排行榜", "哄睡", "故事", "儿歌", "科普", "国学", "动画"]
        try:

            child_id = request.query_params["child_id"]
            test = cla_list[int(child_id)]
        except:
            XMLYException({"code":5000,"msg":"页面信息不存在"})

        queryset = self.get_queryset()  # 得到所有节目的集合
        fic_queryset = queryset.filter(nav_id=2)  # 过滤出儿童的节目

        pro_list = []  # 定义存储儿童节目信息列表

        for temp in fic_queryset:
            kind = temp.pro_type_id % 10

            if int(request.query_params["child_id"]) == kind:
                # 组装数据
                pro_one_dict = {
                    "id": temp.id,
                    "pro_img": temp.pro_img,
                    "pro_name": temp.pro_name,
                    "pro_intro": temp.pro_intro
                }
                pro_list.append(pro_one_dict)
        result = {
            "data": pro_list
        }

        return Response(result)

    #历史子版块   GET 传参  child_id
    @list_route(methods=["GET"])
    def history_child(self, request):

        cla_list = ["排行榜","败家讲坛","中国史","世界史","名人传","侃野史","三国"]

        #检测该子类是否存在
        try:
            child_id = request.query_params["child_id"]
            test = cla_list[int(child_id)]
        except:
            raise XMLYException({"code": 5000, "msg": "您访问的页面不存在"})


        queryset = self.get_queryset()  # 得到所有节目的集合
        fic_queryset = queryset.filter(nav_id=3)  # 过滤出历史的节目

        pro_list = []  # 定义存储历史节目信息列表

        for temp in fic_queryset:
            kind = temp.pro_type_id % 10 #获取节目分类

            if int(request.query_params["child_id"]) == kind: #根据用户 发送的分类id 匹配
                # 组装数据
                pro_one_dict = {
                    "id": temp.id,
                    "pro_img": temp.pro_img,
                    "pro_name": temp.pro_name,
                    "pro_intro": temp.pro_intro
                }
                pro_list.append(pro_one_dict)
        result = {
            "data": pro_list
        }
        #返回数据
        return Response(result)

#节目板块
class ProViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, mixins.DestroyModelMixin):

    queryset = Program.objects.all()  # 从节目表得到结合
    serializer_class = ProSerializer  # 将节目表序列化

    #节目处理方法
    @list_route(["GET"],serializer_class=DetailsSerializer)
    def pro_info(self,request):
        #获取 get请求中节目的id  ：pro_id
        try:
            pro_id = request.query_params["pro_id"]
        except:
            raise XMLYException({"code":5000,"msg":"您访问的页面不存在！"})
        #从节目集合中过滤出参数id 对应的节目

        pro = self.queryset.filter(id = pro_id).first()#过滤出节目信息

        if not pro:
            raise XMLYException({"code":5001,"msg":"节目信息不存在！"})
        #组装节目信息
        pro_dict= {
            "pro_id":pro.id,
            "pro_name":pro.pro_name,
            "pro_img":pro.pro_img,
            "pro_intro":pro.pro_intro,
        }

        #通过节目id 从节目详情中过滤出对应节目详情信息
        pro_detail_queryset = Details.objects.filter(program_id= pro.id)

        #将节目详情序列化
        ser_pro_detail = self.get_serializer(pro_detail_queryset,many=True)

        #组装发送数据
        result = {
            "pro":pro_dict,
            "detail_data":ser_pro_detail.data
        }
        return Response(result)

#节目详情板块

class DetailProViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, mixins.DestroyModelMixin):

    queryset = Details.objects.all()#关联数据库节目详情模型
    serializer_class = DetailsSerializer#关联节目详情序列化类

    #处理节目详情 GET 方式传参 ：detail_id  节目详情id
    @list_route(methods=["GET"])
    def detail_pro(self,request):

        #检测参数是否传入正确
        try:
            detail_pro_id = request.query_params["detail_id"]#获取节目详情的id
        except:
            raise XMLYException({"code":5000,"msg":"您访问的页面不存在！"})

        queryset = self.get_queryset() #得到节目详情集合

        detail_one = queryset.filter(id = int(detail_pro_id)).first()#根据id获取节目详情

        #检测能否查到节目信息
        if  not detail_one:
            raise XMLYException({"code": 5002, "msg": "节目详细信息不存在！"})
        #节目信息序列化
        ser_detail = self.get_serializer(detail_one)
        #返回响应
        return  Response(ser_detail.data)





















