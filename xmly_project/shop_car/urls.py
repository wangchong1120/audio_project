from rest_framework.routers import SimpleRouter


from shop_car.views import CartViewSet


cart_router = SimpleRouter()
cart_router.register(r'cart',CartViewSet)


