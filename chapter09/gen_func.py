# -*- coding: utf-8 -*-
from collections import UserList

# 调用生成器函数，返回生成器对象，python编译字节码的时候产生了
# 通过yield使实现协程成为可能
# 惰性求值，延迟求值成为可能


def gen_fun():
    yield 1
    yield 2
    yield 3


def func():
    return 1


# def fibonacci(index):
#     if index in [1, 2]:
#         return 1
#
#     x1, x2 = 1, 1
#
#     for i in range(3, index + 1):
#         x1, x2 = x2, x1 + x2
#         yield x1

def fib(index):
    res_list = []
    n, a, b = 1, 1, 1

    while n < index:

        a, b = b, a+b  # python解包
        res_list.append(a)
        n += 1
    return res_list


def gen_fib(index):
    n, a, b = 0, 0, 1

    while n < index:
        yield b
        a, b = b, a + b  # python解包
        n += 1


if __name__ == '__main__':
    gen = gen_fun()

    # for value in gen:
    #     print(value)
    # re = func()
    # pass

    # print(fib(3))
    for res in gen_fib(10):
        print(res)
