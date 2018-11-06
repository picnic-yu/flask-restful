


from app.libs.redprint import Redprint

#redprint

api = Redprint('book')

@api.route('/book')
def get_book():
    return 'book'