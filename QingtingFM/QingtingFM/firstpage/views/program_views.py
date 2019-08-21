from rest_framework import viewsets,mixins
from rest_framework.response import Response

from firstpage.filters import ProgramFilter
from firstpage.serializers import *

#节目详情视图集类
class ProgramViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Mainshow.objects.all()
    serializer_class = MainshowSerializer
    filter_class = ProgramFilter            # 绑定的过滤器类

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        ser = self.get_serializer(queryset, many=True)

        program_details=[]
        title_id = request.query_params.get("title_id")               #接收请求的title
        programlist = Programlist.objects.filter(title_id=title_id)   #通过title过滤查询符合条件的章节列表
        for program in programlist:                                   #遍历每个章节信息，组装成字典
            program_detail = [{"program_name":program.program_name,"audio_id":program.audio_id,"audio_href":program.audio_href,
                               "duration":program.duration,"loopnumber_program":program.loopnumber,"upload_time":program.upload_time}]
            program_details.append(program_detail)
        result = {
            "content" : ser.data,
            "program_details" : program_details,
        }
        return Response(result)     #返回音频的具体信息页面的数据


class ProgramtuijianViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Mainshow.objects.all()
    serializer_class = MainshowSerializer
    filter_class = ProgramFilter            # 绑定的过滤器类

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        ser = self.get_serializer(queryset, many=True)

        program_details=Mainshow.objects.all()
        result = {
            "content" : ser.data,
            "program_tuijian" : MainshowSerializer(instance=program_details, many=True).data[-10::-2]
        }
        return Response(result)     #返回音频的具体信息页面的数据




