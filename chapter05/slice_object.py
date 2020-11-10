# -*- coding: utf-8 -*-
from collections.abc import Sequence
import numbers
# print(dir(list))


class Group:
    """实现可切片的不可变序列类型"""
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __getitem__(self, item):
        return self.staffs[item]

    def __getitem__(self, item):
        """切片后生成group对象"""
        # return self.staffs[item]

        # 获取
        cls = type(self)  # 尽量不要使用硬编码

        if isinstance(item, slice):  # 切片
            return cls(company_name=self.company_name,
                       group_name=self.group_name,
                       staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):  # 索引
            return cls(company_name=self.company_name,
                       group_name=self.group_name,
                       staffs=[self.staffs[item]])

    def __reversed__(self):
        # return self.staffs.reverse()
        self.staffs.reverse()

    def __len__(self):
        return len(self.staffs)  # 委托给list

    def __contains__(self, item):
        return True if item in self.staffs else False

    def __iter__(self):
        return iter(self.staffs)


if __name__ == '__main__':
    employees = ["Booby", "Tom", "Sandy", "Jam"]
    group = Group(company_name="mooc", group_name="user", staffs=employees)
    sub_group = group[:2]
    sub_group = group[0]
    # for staff in sub_group.staffs:
    #     print(staff)

    reversed(group)
    # print(group)
    print(len(group))

    if "Tom" in group:
        print("Yes -_-")

    for user in group:
        print(user)