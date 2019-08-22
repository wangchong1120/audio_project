

from rest_framework.routers import SimpleRouter

from user.views import UserViewSet

user_router=SimpleRouter()

user_router.register(r'user',UserViewSet)