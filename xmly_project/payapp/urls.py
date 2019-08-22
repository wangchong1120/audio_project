from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from payapp import views
from payapp.views import OrderViewSet, OrderPayView, CheckPayView

from django.urls import path



urlpatterns = [
    url(r'orderspay/',OrderPayView.as_view()),
    url(r'checkpay/',CheckPayView.as_view())

]

pay_router = SimpleRouter()
pay_router.register(r'orders',OrderViewSet)


urlpatterns += pay_router.urls