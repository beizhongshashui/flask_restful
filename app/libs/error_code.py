from app.libs.error import APIException


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

class ParameterException(APIException):

    code = 400
    msg = 'parameter is error.'
    error_code = 1000

class ClientException(APIException):

    msg = 'paramery is error'
    code = 402
    error_code = 1002

class Success(APIException):
    code = 201
    msg = 'Success'
    error_code = 200