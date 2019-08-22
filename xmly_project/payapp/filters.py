import django_filters

from payapp.models import ORDER_STATE_NO_PAY, ORDER_STATE_NO_SEND


class OrdersFilter(django_filters.rest_framework.FilterSet):
    #等号做表边的类属性名对应于前端传递过来的过滤参数名
    o_status = django_filters.CharFilter(method='filter_status')

    def filter_status(self,queryset,name,value):
        if value == 'all':
            return queryset
        elif value == 'not_pay':
            return queryset.filter(o_state=ORDER_STATE_NO_PAY)
        elif value == 'not_send':
            return queryset.filter(o_state = ORDER_STATE_NO_SEND)

