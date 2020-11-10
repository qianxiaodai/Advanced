# -*- coding: utf-8 -*-

# from collections.abc import Iterable, Iterator
from _collections_abc import Iterable, Iterator


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):  # 定义了__iter__, 返回Iterator对象
        return iter(self.employee)

    def __getitem__(self, idx):
        return self.employee[idx]


if __name__ == '__main__':

    company = Company(["tom", "bob", "jane"])  # 遍历

    # iter(item) python解释器内部做的，会去寻找类中是否定义了__iter__魔法函数，
    for item in company:
        print(item)
