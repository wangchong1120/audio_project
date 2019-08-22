import django_filters


class ProFilter(django_filters.rest_framework.FilterSet):#定义节目过滤器类

    #定义男女生喜欢过滤字段
    #boy_girl_like
    is_boy = django_filters.CharFilter("filter_boy_girl")
    is_good = django_filters

    def filter_boy_girl(self,queryset,name,value):

        if value == "1":
            return queryset.filter(is_boy=0)
        else:
            return queryset.filter(is_boy=value)
