"""xmly_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xmly_project.settings")# project_name 项目名称
django.setup()
from django.contrib import admin
from django.urls import path,include

from I_listen_app.urls import listen_router
from home_page.urls import main_router
from payapp.urls import pay_router
from shop_car.urls import cart_router
from user.urls import user_router

urlpatterns = [
    path('admin/',admin.site.urls),
    path('shop_car/',include(cart_router.urls)),
    path('shop_mall/',include('shop_mall.urls')),
    path('I_listen_app/',include(listen_router.urls)),
    path('payapp/',include('payapp.urls')),
    path('api/xmly/',include(main_router.urls)),
    path('api/',include(user_router.urls))
]
