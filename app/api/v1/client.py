
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from app.libs.enums import ClientTypeEnum
from flask import request, jsonify
api = Redprint('client')
@api.route('/register',methods=['post'])
def create_client():
    # 注册 登陆
    # 表单 json
    # 网页 移动端
    # 获取数据方式   1. data = request.json 2.request.args.to_dict()
    data = request.json
    form = ClientForm(data = data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email
        }
    return 'xixihaha'


def __register_user_by_email():
    pass