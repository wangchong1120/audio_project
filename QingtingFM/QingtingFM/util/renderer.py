from rest_framework.renderers import JSONRenderer

class QTFMRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            code = data.pop("code")   #处理过程有问题，才会弹出code,msg
            msg = data.pop("msg")
        except:
            code = 200
            msg = "ok"
            
        renderer_context['response'].status_code = 200    #无论如何都将HTTP协议状态码改为200
        result = {
            "code":code,
            "msg":msg,
            "data":data
        }
        return super().render(result)
