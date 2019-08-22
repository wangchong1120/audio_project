from rest_framework.renderers import JSONRenderer

class XMLYRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            code = data.pop('code')
            msg = data.pop('msg')
        except:
            code = 200
            msg = 'ok'
        renderer_context['response'].status_code = 200
        result={
            'code':code,
            'msg':msg,
            'data':data
        }
        return super().render(result)
