from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication


#封装进行Token验证的方法，并且在底层进行返回一个元组
from user.models import XMLYUser
from util.errors import XMLYException

"""
class BaseAuthentication(object):
    #All authentication classes should extend BaseAuthentication.
    

    def authenticate(self, request):
        
        #Authenticate the request and return a two-tuple of (user, token).
        
        raise NotImplementedError(".authenticate() must be overridden.")
"""
class UserTokenAuthentication(BaseAuthentication):
    #复写  def authenticate(self, request): 方法
    def authenticate(self, request):
        try:
            token = request.data.get('token') if request.data.get('token') else request.query_params.get('token')
            use_id=cache.get(token)
            user=XMLYUser.objects.get(pk=use_id)
            return (user,token)   # 自动赋值   request.user=user   request.auth=token
        except:
            raise XMLYException({'code':6666,'msg':'还未登录，无权进行该操作!!!'})
