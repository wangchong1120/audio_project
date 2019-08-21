from rest_framework.routers import SimpleRouter

from myapp.views import MainShowSet, ChildViewSet, ProViewSet, DetailProViewSet



main_router = SimpleRouter()
main_router.register(r'mainshow',MainShowSet)
main_router.register(r'child',ChildViewSet)
main_router.register(r'pro',ProViewSet)
main_router.register(r'detail',DetailProViewSet)



