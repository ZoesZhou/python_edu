# import bisect
#
# lst = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51, 100]
#
# newlst = sorted(lst)
# print(newlst)
#
# for x in (20, 30, 40, 100):
#     bisect.insort_left(newlst, x)
#     print(newlst)
#
#
# def get_grade(score):
#     level = 'EDCBA'
#     score_level = [60, 70, 80, 90]
#     index = bisect.bisect(score_level, 62)
#     return level[index]
#
#
# print(get_grade(62))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def is_empty(self):
#         return self.head is None
#
#     def append(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#
#     def iter(self):
#         if not self.head:
#             return
#         cur = self.head
#         yield cur.data
#         while cur.next:
#             cur = cur.next
#             yield cur.data
#
#
# link_list = LinkedList()
# for i in range(10):
#     link_list.append(i)
#
# for x in link_list.iter():
#     print(x)
#


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         node = Node(data)
#         if self.head is None:  # 空链表，增加第一个元素
#             self.head = node
#         else:
#             pointer = self.head  # 指针位置在头部
#             while pointer.next is not None:  # 找到尾部，尾部的next指向要添加的数据
#                 pointer = pointer.next
#             pointer.next = node
#
#     def iter_nodes(self):
#         pointer = self.head
#         while pointer is not None:
#             print(pointer)
#             pointer = pointer.next
#         # print('Null')
#
#
# li = LinkedList()
# li.append(5)
#
# li.iter_nodes()


# def fib():
#     a = 0
#     b = 1
#     i = 0
#     while i < 100:
#         i += 1
#         a, b = b, a + b
#         print(a)
#
#
# fib()


# class Fib:
#     def __call__(self, *args, **kwargs):
#         pass
#
#
# f = Fib()
# print(f(5))
#
#
# def fib():
#     ret = [1, 1]
#


import time
import datetime


# def show_time(fn):
#     def _show(*args):
#         start = datetime.datetime.now()
#         ret = fn(*args)
#         stop = datetime.datetime.now()
#         print((start - stop).total_seconds())
#         return ret
#     return _show()
#
#
# @show_time  # add = show_time(add)
# def add(x, y):
#     time.sleep(2)
#     return x + y


# print(add(4, 5))


# class ShowTime:
#     def __init__(self, fn):
#         print('init')
#         self.fn = fn
#
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         stop = datetime.datetime.now()
#         print((self.start - stop).total_seconds())
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#         start = datetime.datetime.now()
#         ret = self.fn(*args, **kwargs)
#         stop = datetime.datetime.now()
#         print((start - stop).total_seconds())
#         return ret
#
#
# @ShowTime  # add=Show()(add)
# def add(x, y):
#     time.sleep(2)
#     return x + y


# a = add(4, 5)
# with a as f:


# from contextlib import contextmanager
#
#
# @contextmanager
# def foo():
#     print('enter')
#     yield 100
#     print('exit')
#
#
# with foo() as f:
#     print('---------')
#     print(f)
#     print('==========')


# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#
# class B:
#     x = A()
#
#     def __init__(self):
#         print('B.init')
#
#
# print('-'*30)
# print(B.x.a1)
# print('='*20)
# b = B()
# print(b.x.a1)


# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#     def __get__(self, instance, owner):
#         print('A.__get__{} {} {}'.format(self, instance, owner))
#         # print(instance)  # 表示B的实例
#         # print(owner)  # owner都是B的类
#         print(self)
#         # return self  # self就是A的实例
#         return instance.z
#
#     def __set__(self, instance, value):
#         print('A.__set__{} {} {}'.format(self, instance, value))
#         # self.data = value
#         instance.z = value
#         # instance.x = value  # 递归了
#
#
# class B:
#     x = A()
#     y = 1
#
#     def __init__(self):
#         print('B.init')
#         # self.x = A()  # 触发__set__
#         self.x = '1'  # 触发__set__
#         # self.n = A()  # 没有触发__set__
#
#
# # print('-'*20)
# # print(B.x.a1)
# # print('='*20)
# b = B()  # 触发__set__
# print(b.x)
# print(b.__dict__)
# print(B.__dict__)
# # print(b.x)  # 触发 __get__
# # print(b.x.a1)
# # b.x = 1
# # print(b.__dict__)
# # print(b.x.a1)
# # print(A().__dict__)
# # b.x = 1
# # b.x
# # print(b.__dict__)
# # B.x
# # B.x = 1
# # print(B.x)


# class A:
#     @classmethod
#     def foo(cls):
#         pass
#
#     @staticmethod
#     def bar():
#         pass
#
#     @property
#     def z(self):
#         return 5
#
#     def getfoo(self):
#         return self.foo
#
#     def __init__(self):
#         self.foo = 100
#         self.bar = 200
#         self.z = 300
#
#
# a = A()
# print(a.z)
# print(a.__dict__)
# print(A.__dict__)


# class StaticMethod:
#     def __init__(self, fn):
#         # pass
#         self.fn = fn
#
# # self = StaticMethod(fn),instance = A(),owner = A
#     def __get__(self, instance, owner):
#         # pass
#         # return self
#         return self.fn
#
#
# class A:
#     @StaticMethod  # foo = StaticMethod(foo) 类的实例化
#     def foo():  # 现在这个foo是StaticMethod的实例
#         print('static method called')
#
#
# a = A()
# a.foo()  # 属主的实例访问属主的类属性触发__get__,原函数foo,
# # 现在被StaticMethod的实例属性记住了，return 回去就可以了
#
# from functools import partial
#
#
# class ClassMethod:
#     def __init__(self, fn):
#         print('init====')
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         print('get-----')
#         return partial(self.fn, owner)
#
#
# class A:
#     @ClassMethod  # bar = ClassMethod(bar) 对应实例化，初始化
#     def bar(cls):
#         print('class method called')
#
#
# A.bar()  # A.bar要返回一个函数，用偏函数，触发__get__
#
#
# class Property:
#
#     def __init__(self, fn):  # data=Property(fn)
#         self.fn = fn
#         self.fn_s = None
#
#     def __get__(self, instance, owner):  # instance = A(5),owner=A
#         if instance is not None:
#             return self.fn(instance)
#
#     def __set__(self, instance, value):
#         if callable(self.fn_s):
#             self.fn_s(instance, value)
#         else:
#             raise AttributeError('{} can not assign'.format(self.fn_s.__name__))
#
#     def setter(self, fn):  # self = Property(data)
#         self.fn_s = fn  # 这是为实例增加属性，对应一个函数，不会绑定
#         return self
#
#
# class A:
#     def __init__(self, data):
#         self._data = data
#
#     @Property  # data = Property(data);data = data.getter(data)
#     def data(self):  # data是Property的实例，然后data被返回的值覆盖
#         return self._data
#
#     @data.setter  # data = data.setter(data)
#     def data(self, value):
#         self._data = value
#
#
# a = A(5)
# print(a.data)
# a.data = 10
# print(a.data)
























































