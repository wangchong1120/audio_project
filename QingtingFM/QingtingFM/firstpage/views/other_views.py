from rest_framework import viewsets,mixins
from rest_framework.response import Response

from firstpage.filters import ProgramFilter
from firstpage.serializers import *

# 全部分类
from util.errors import QTFMException


class NavViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = Nav.objects.all()
    serializer_class = NavSerializer


class SearchViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Mainshow.objects.all()
    serializer_class = MainshowSerializer

    def list(self, request, *args, **kwargs):
        title = request.query_params.get("title")  # 接收请求的title
        mainshowlist = Mainshow.objects.filter(title__contains=title)
        if mainshowlist:
            result = {
                "content" : MainshowSerializer(instance=mainshowlist, many=True).data
            }
            return Response(result)
        raise QTFMException({
            "code" : 303,
            "msg" : "没有查找到与您搜索匹配的音频，请重新输入"
        })

