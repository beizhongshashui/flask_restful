from app.libs.enums import ClientEnums
from app.libs.redprint import Redprint
from flask import request
from app.validators.forms import ClientForm, UserClientForm
from app.model.user import User
from app.libs.error_code import ClientException,ParameterException

api = Redprint('client')

@api.route('/clients',methods = ['GET'])
def clientlist():

    return  'secuess'

@api.route('/register',methods=['POST'])
def create_client():
    #客户端提交数据的方式是多样的，有xml json 表单
    form = ClientForm().validate_for_api()

    promise = {
        ClientEnums.USER_EMAIL : register_by_email
    }
    print(form.type.data)
    promise[form.type.data]()

    return 'success.'

def register_by_email():


    form = UserClientForm().validate_for_api()
    print('form = ',form)
    User.register_by_email(form.nickname.data,form.account.data,form.secret.data)