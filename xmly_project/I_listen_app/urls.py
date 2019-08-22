from rest_framework.routers import SimpleRouter

from I_listen_app.views import ListenSingleViewSet, DownloadViewSet

listen_router = SimpleRouter()
listen_router.register(r'listensingl',ListenSingleViewSet)
listen_router.register(r'download',DownloadViewSet)