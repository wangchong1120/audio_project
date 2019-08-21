from rest_framework.exceptions import APIException

class XMLYException(APIException):
    def __init__(self,msg):
        self.detail = msg