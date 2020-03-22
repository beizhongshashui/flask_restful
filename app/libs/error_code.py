from app.libs.error import APIException


class ClientException(APIException):

    msg = 'paramery is error'
    code = 402
    error_code = 1002