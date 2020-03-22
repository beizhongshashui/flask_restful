from app.libs.error import APIException


class ClientException(APIException):

    msg = 'paramery is error'
    code = 402
    error_code = 1002


class ParameterException(APIException):

    code = 400
    msg = 'parameter is error.'
    error_code = 1000