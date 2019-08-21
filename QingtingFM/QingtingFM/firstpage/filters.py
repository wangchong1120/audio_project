import django_filters

from firstpage.models import *

# 音频节目过滤器类
class ProgramFilter(django_filters.rest_framework.FilterSet):
    # 等号左边为前端传递的过滤参数，右边为模型表中的字段名
    title_id = django_filters.CharFilter("title_id")

    class Meta:
        model = Mainshow
        fields = ["title","title_id"]


class AudioFilter(django_filters.rest_framework.FilterSet):
    audio_id = django_filters.CharFilter("audio_id")

    class Meta:
        model = Programlist
        fields = ["audio_id"]