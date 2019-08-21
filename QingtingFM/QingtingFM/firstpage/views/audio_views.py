from rest_framework import viewsets,mixins
from rest_framework.response import Response

from firstpage.filters import AudioFilter
from firstpage.serializers import *

#节目详情视图集类
class AudioViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Programlist.objects.all()
    serializer_class = ProgramlistSerializer
    filter_class = AudioFilter            # 绑定的过滤器类

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        ser = self.get_serializer(queryset, many=True)
        audio_show = ser.data[0]

        title_id = audio_show['title_id']
        program = Mainshow.objects.filter(title_id=title_id)
        for i in program:
            img_program = i.img
            title_program = i.title
        content=[{"img":img_program,"program_name":title_program +"-"+ audio_show['program_name'],
                  "audio_href":audio_show["audio_href"],"loopnumber":audio_show["loopnumber"],}]
        result = {
            "content" : content,
        }
        return Response(result)


