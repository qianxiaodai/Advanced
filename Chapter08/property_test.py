# -*- coding: utf-8 -*-

from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday


user = User("bobby", date(year=1993, month=9, day=30))
print("in {file_name} file".format(file_name=__file__))


if __name__ == '__main__':
    pass