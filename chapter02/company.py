# -*- coding: utf-8 -*-
"""
需求：遍历公司每个员工
魔法函数：python中定义的以__开头，__结尾的函数
定制类的特性
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])  # 遍历

# company = company[:2]
# employee = company.employee

print(len(company))

# for em in company:
#     print(em)