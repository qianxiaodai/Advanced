# -*- coding: utf-8 -*-
# from collections.abc import *
from _collections_abc import __all__


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        # 参数必须传进去，否则会报错
        return super().__new__(cls, *args, **kwargs)  # 直接调用父类的__new__()方法
        pass


class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"


if __name__ == '__main__':
    user = User("booby")
    print(user)
    pass