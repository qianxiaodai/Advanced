# -*- coding: utf-8 -*-
"""
python中一切皆对象，

"""


class Person(object):
    def __init__(self):
        print("class:\t  bobby")


def ask(name="bobby"):
    print("function:", name)


# 函数作为函数的返回值
def decorator_func():
    print("dec start")
    return ask


my_ask = decorator_func()
my_ask("Tom")

# 函数和类可以添加到集合对象中
# obj_list = list()
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     item()


# my_func = ask  # 函数可以赋值给对象
# my_func()
#
#
# my_class = Person  # 类可以赋值给变量
# my_class()

