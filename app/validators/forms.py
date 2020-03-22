from  wtforms import StringField,IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp,ValidationError
from app.model.user import User
from app.libs.enums import ClientEnums
from app.validators.base import BaseForm as Form


class ClientForm(Form):

    account = StringField(validators=[DataRequired(),length(max=24,min=8)])
    secret = StringField()
    type = IntegerField(DataRequired())

    def validate_type(self,value):
        print('validate_type == ',value.data)
        try:
            client = ClientEnums(value.data)
        except ValueError as e:
            # print('e = ',e)
            raise e
        # print('client == ',client)
        self.type.data = client


class UserClientForm(Form):

    account = StringField(validators=[DataRequired(),Email(message='invalidate email.')])

    secret = StringField(validators=[DataRequired(),Regexp(r'^[a-zA-Z0-9_*$&#@]{6,22}')])

    nickname = StringField(validators=[DataRequired(),length(min=4,max=30)])

    def validate_account(self,value):

        if User.query.filter_by(email=value.data).first():
           raise ValidationError()
