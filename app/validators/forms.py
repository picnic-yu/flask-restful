from wtforms import Form
from app.libs.enums import ClientTypeEnum

class ClientForm(Form):
    account = StringField(validators=[DataRequired(),length(
        min=5,max=32
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])
    # 自定义验证器
    def validate_type(self,value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        