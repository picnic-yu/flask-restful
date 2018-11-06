

from app.libs.redprint import Redprint
api = Redprint('user')


@api.route('/user')

def get_test():
    return 'xixihaha'