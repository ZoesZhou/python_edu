# class Animal:
#     x = 23
#
#     def __init__(self, name):
#         self.name = name
#         self.__age = 10
#         self.weight = 20
#
#
# print('animal Module\'s names = {}'.format(dir()))  # 模块的属性


# class A:
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#         print(*args)
#         print(**kwargs)
#         # return None
#         # return 1
#         return super().__new__(cls)  # 调用父类的__new__来生成实例
#
#     def __init__(self, name):
#         self.name = name
#         print('---------')
#
#
# a = A('1')
# print(a)


# class A:
#     def __init__(self, name, age=18):
#         self.name = name
#
#     def __hash__(self):
#         return 1
#
#     def __eq__(self, other):
#         return self.name == other.name  # 等价于return True
#         # return True
#
#     def __repr__(self):
#         return self.name
#
#
# print(hash(A('tom')))
# print((A('tom'), A('tom')))
# s = {A('tom'), A('tom')}
# print(s)
# print({'tom', 'tom'})
# print({tuple('t'), tuple('t')})


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#         # return True
#
#
# p1 = Point(2, 3)
# p2 = Point(2, 3)
# print(1, p1)
# print(2, p2)
# print(p1 == p2)
# print(p1 is p2)
# print(3, set((p1, p2)))
# print(4, {p1, p2})
# from collections import Hashable
# print(isinstance(p1, Hashable))


# class A: pass
#
#
# print(bool(A()))
# if A():
#     print('1')
#
#
# class B:
#     def __bool__(self):
#         return False
#
#
# print(bool(B))
# print(bool(B()))
# if B():
#     print('2')
#
#
# class C:
#     def __len__(self):
#         return 0
#
#
# print(bool(C()))
# if C():
#     print('3')


# class A:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return 'repr: {}, {}'.format(self.name, self.age)
#
#     def __str__(self):
#         return 'str: {}, {}'.format(self.name, self.age)
#
#     def __bytes__(self):
#         import json
#         return json.dumps(self.__dict__).encode()
#
#
# print(A('tom'))  # str
# print([A('tom')])  # repr
# print([str(A('tom'))])  # str
#

# class A:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
#     def __sub__(self, other):
#         return self.age - other.age
#
#     def __isub__(self, other):
#         # return A(self.name, self - other)
#         return self.__class__(self.name, self - other)
#         # self-other就是tom-jerry, 调用__sub__
#
#
# tom = A('tom')
# jerry = A('jerry', 16)
# print(tom - jerry)
# print(jerry - tom, jerry.__sub__(tom))
# print(id(tom))
# tom -= jerry
# print(tom)
# print(tom.age, id(tom))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return '<Point: {}, {}>'.format(self.x, self.y)
#
#
# p1 = Point(1, 1)
# p2 = Point(1, 1)
# print(p1+p2)
# print(p1 == p2)


# from functools import total_ordering
#
#
# @total_ordering
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
#     # def __gt__(self, other):
#     #     return self.age > other.age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#
# tom = Person('tom', 20)
# jerry = Person('jerry', 16)
#
# print(tom > jerry)
# print(tom >= jerry)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
#     def __gt__(self, other):
#         return self.age > other.age
#
#     def __ge__(self, other):
#         return self.age >= other.age
#
#
# tom = Person('tom', 20)
# jerry = Person('jerry', 16)
# print(tom > jerry)
# print(tom >= jerry)
# print(tom == jerry)
# print(tom != jerry)


# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, item):
#         self.items.append(item)
#
#     def __getitem__(self, index):  # 索引访问
#         return self[index]
#
#     def __setitem__(self, key, value):  # 索引赋值
#         self.items[key] = value
#
#     def __iter__(self):
#         # return iter(self.items)
#         yield from self.items
#
#     def __add__(self, other):  # 实例就是容器
#         self.items.append(other)  #
#         return self
#
#     def __len__(self):
#         return len(self.items)
#
#     def __str__(self):
#         # return '{}'.format(self.items)
#         return str(self.items)
#
#
# cart = Cart()
# cart.add_item(1)
# cart.add_item('2')
# cart.add_item(3)
# print(cart)
# for i in cart:
#     print(i)
#
# cart + 5 + 9
# print(cart.__add__(17).__add__(18))
# print(cart)
# print(len(cart))
# print(bool(cart))
#
# cart[1] = 0
# print(cart)
# print(0 in cart)

# def command_dispatcher():
#     # 注册函数
#     cmd_dict = {}
#
#     def reg(cmd):
#         def _reg(fn):
#             cmd_dict[cmd] = fn
#             return fn
#
#         return _reg
#
#     # 默认函数
#     def default_fn():
#         print('unknow command')
#
#     # 命令分发
#     def dispatcher():
#         while True:
#             cmd = input('>>')
#             if cmd == 'q':
#                 break
#             cmd_dict.get(cmd, default_fn)()
#
#     return reg, dispatcher
#
#
# reg, dispatcher = command_dispatcher()
#
#
# @reg('1')
# def foo1(x=4, y=5, z=6):
#     print(x + y + z)
#
#
# @reg('2')
# def foo2(x=4, y=5):
#     print(x * y)
#
#
# dispatcher()
#
#
# class Dispatcher:  # 把类当装饰器
#     def __init__(self, cmd):
#         self.cmd = cmd
#
#     def reg(self, cmd, fn):
#         self.cmd =
#
#     def run(self):
#
#
# def add():
#
#
#
#
# d = Dispatcher('a')
# setattr(Dispatcher, 'b', c)
# print(getattr(d, 'a'))
#


# class StaticMethod:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __get__(self, instance, owner):  # instance=None
#         print(self, instance, owner)
#         return self.fn
#
#
# class A:
#     @StaticMethod  #foo=StaticMethod(foo)
#     def foo():
#         print('Static method called')
#
#
# a = A()
# a.foo()

from functools import partial


# class ClassMethod:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         print(self, instance, owner)
#         return partial(self.fn, owner)
#
#
# class A:
#     @ClassMethod  # foo=StaticMethod(bar)(cls)
#     def bar(cls):
#         print('Class method called')
#
#
# a = A()
# a.bar()

import inspect


class TypeCheck:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.data = {}

    def __get__(self, instance, owner):
        if instance is not None:
            print(self.__dict__)



# def typeassert(cls):
#     sig = inspect.signature(cls)
#     params = sig.parameters
#
#     for name, param in params.items():
#         if param.annotation != param.empty:
#             setattr(cls, name, TypeCheck(name, param.annotation))
#     return cls


class TypeAssert:
    def __init__(self, cls):
        sig = inspect.signature(cls)
        params = sig.parameters

        for name, param in params.items():
            if param.annotation != param.empty:
                setattr(cls, name, 1)
        self.cls

    def __call__(self, ):
        pass


@TypeAssert  # Person = TypeAssert(Person)
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


p = Person('tom', 18)







































