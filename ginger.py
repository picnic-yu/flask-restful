'入口文件'
from app.app import create_app

app = create_app()

@app.route('/v1/user/test')
def get_test():
    return 'xixihaha'
if __name__ == '__main__':
    app.run(debug = True)