

class CustomMetaClass(type):
    def __init__(cls, what, bases=None, dict=None):
        print('CustomMetaClass.__init__cls:', cls)
        super().__init__(what, bases, dict)

    def __call__(cls, *args, **kwargs):
        print('CustomerMetaClass.__call__args:', args, kwargs)
        self = super(CustomMetaClass, cls).__call__(*args, **kwargs)
        print('CustomerMetaClass.__call__self:', self)
        return self


class CustomClass(metaclass=CustomMetaClass):
    def __init__(self, *args, **kwargs):
        print('CustomClass.__init__self:', self)
        super().__init__()

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        print('CustomClass.__new__, self:', self)
        return self

    def __call__(self, *args, **kwargs):
        print('CustomClass.__call__args:', args, **kwargs)


obj = CustomClass('arg1', 'arg2', kwargs1=1, kwarg=2)
print(type(CustomClass))
print(obj)
obj('arg1', 'arg2')


