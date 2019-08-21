from rest_framework.exceptions import APIException

class QTFMException(APIException):

    def __init__(self,msg):
        self.detail = msg