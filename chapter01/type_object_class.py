# -*- coding: utf-8 -*-

a = 1
b = "abc"
print(type(1))
print(type(int))
print(type(b))
print(type(str))

# type->int->1  type
# type->class->obj

# object是最顶层基类

class Student(object):
    pass


class MyStudent(Student):
    pass


stu = Student()
print(type(stu))
print(type(Student))
print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(MyStudent.__bases__)
print(type.__bases__)
print(object.__bases__)
print(type(object))
