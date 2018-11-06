class Redprint:
    def __init__(self, name):
        self.name = name
        self.mound = []
    # 实现route装饰器
    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f,rule,options))
            # 存起来到注册那边把视图函数向蓝图的注册
            return f
        return decorator
    def register(self, bp, url_prefix = None):
        if url_prefix == None:
            url_prefix = '/'+self.name
        for f, rule, options in self.mound:
            endpoint = options.pop('endpoint',f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)