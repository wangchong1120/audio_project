from django.urls import path
from rest_framework.routers import SimpleRouter

from firstpage.views import *

router = SimpleRouter()
router.register(r'detail/detailjiemu',ProgramViewSet)   #音频详情页面节目栏
router.register(r'detail/detailtuijian',ProgramtuijianViewSet)  #音频详情页面推荐栏
router.register(r'detail',ProgramViewSet)   #音频详情页面

router.register(r'search/searchIndex',SearchViewSet)     # 搜索页面
router.register(r'search/searchDetail',ProgramViewSet)     # 搜索页面跳转

router.register(r'open/open',AudioViewSet)  #播放页面
router.register(r'allNav',NavViewSet)   #全部分类

urlpatterns = [
    path('index/tuijian/',tuijian_view),    #推荐页面
    path('xiaoshuo/', xiaoshuo_view),       #小说页面
    path('xiaoshuo/xiaoshuoman/',xiaoshuo_view), #小说男生页面
    path('xiaoshuo/aztuijian/', xiaoshuo_view),  # 小说男生推荐页面
    path('xiaoshuo/reting/',xiaoshuo_reting_view),   #小说热听
    path('xiaoshuo/xiaoshuowomen/',xiaoshuo_girl_view), #小说女生页面
    path('xiaoshuo/womentuijian/', xiaoshuo_girl_view),  # 小说女生推荐页面
    path('xiaoshuo/womentchangxiao/',xiaoshuo_changxiao_view),   #小说女生畅销页面
    path('index/pingshu/', pingshu_view),       #评书页面
    path('index/xsxp/', xsxp_view),             #相声小品页面
    path('index/ertong/', ertong_view),         #儿童页面
    path('index/lishi/', lishi_view),           #历史页面
    path('index/wenhua/', pingshu_view),        #文化页面
    path('index/jiaoyu/', pingshu_view),        #教育页面
    path('index/qinggan/', pingshu_view),       #情感页面

]

urlpatterns += router.urls