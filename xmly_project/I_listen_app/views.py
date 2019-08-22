from urllib.request import urlretrieve

from django.http import FileResponse, HttpResponse
from django.shortcuts import render

from rest_framework import viewsets,mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response

from I_listen_app.models import ListenSingle, Download
from I_listen_app.serializers import ListenSerializer, DownloadSerializer
from home_page.models import Details
from user.user_authentication import UserTokenAuthentication
from util.errors import XMLYException


class ListenSingleViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = ListenSingle.objects.all()
    serializer_class = ListenSerializer
    #自关联
    authentication_classes = (UserTokenAuthentication,)

    def list(self, request, *args, **kwargs):
        listensingles = ListenSingle.objects.filter(l_user=request.user)
        ser = self.get_serializer(listensingles,many=True)
        result = {
            'listensingles':ser.data
        }
        return Response(result)
    @list_route(['POST'])
    def add_program(self,request):
        detailsid = request.data.get('detailsid')
        listensingles = ListenSingle.objects.filter(l_user=request.user,l_details_id=detailsid)
        if listensingles:
            return Response({'code':603,'msg':'节目已经存在，无需重复添加！'})
        else:
            try:
                ListenSingle.objects.create(l_user=request.user,l_details_id=detailsid)
            except:
                raise XMLYException({'code':604,'msg':'节目添加失败！'})
            result={
                'data':'节目添加成功'
             }
            return Response(result)

    @list_route(['POST'])
    def sub_program(self,request):
        detailsid = request.data.get('detailsid')
        listensingles = ListenSingle.objects.filter(l_user=request.user, l_details_id=detailsid)
        if listensingles:
            listensingles.delete()
            result = {
                'data': '节目删除成功'
            }
            return Response(result)
        else:
            return Response({'code':605,'msg':'节目不存在，无法删除'})

class DownloadViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer
    #自关联
    authentication_classes = (UserTokenAuthentication,)

    #展示下载页面
    def list(self, request, *args, **kwargs):
        downloads = Download.objects.filter(d_user=request.user)
        ser = self.get_serializer(downloads,many=True)
        result={
            'downloads':ser.data
        }
        return Response(result)

    #添加到下载页面
    @list_route(['POST'])
    def add_download(self,request):
        detailsid=request.data.get('detailsid')
        downloads = Download.objects.filter(d_user=request.user,d_details=detailsid)
        if downloads:
            return Response({'code':606,'msg':'节目已经存在，不需重复下载'})
        else:
            try:
                url=Details.objects.get(pk=detailsid).mp4

                filename='./program/'+url.split('/')[-1]

                urlretrieve(url,filename=filename)
                file=open(filename,'rb')
                response=FileResponse(file)

                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = "attachment;filename=url.split('/')[-1]"

                Download.objects.create(d_user=request.user,d_details_id=detailsid)

                return HttpResponse(response)
            except:
                raise XMLYException({'code':607,'msg':'节目下载失败'})

    #删除下载
    @list_route(['POST'])
    def sub_download(self,request):
        detailsid=request.data.get('detailsid')
        downloads=Download.objects.filter(d_user=request.user,d_details_id=detailsid).first()
        if downloads:
            downloads.delete()
            result = {
                'data': '节目删除成功'
            }
            return Response(result)
        else:
            return Response({'code':608,'msg':'下载文件不存在，无需删除'})

