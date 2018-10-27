# 随机生成整数，指定数值的范围，可以调整没批数字的个数
import random


# # 普通方法
# class RandomGen:
#     def __init__(self, start=1, stop=100, patch=10):
#         self.start = start
#         self.stop = stop
#         self.patch = patch
#
#     def get_number(self):
#         return [random.randint(self.start, self.stop) for _ in range(self.patch)]
#
#
# rg = RandomGen()
# print(rg.get_number())

# 作为工具类来实现，提供类方法
# class RandomGen:
#     def get_number(self, start=1, stop=100, patch=10):
#         return [random.randint(start, stop) for _ in range(patch)]
#
#
# rg = RandomGen()
# print(rg.get_number())


# 使用生成器实现
# class RandomGenerator:
#     def __init__(self, start=1, stop=100, patch=10):
#         self.start = start
#         self.stop = stop
#         self.patch = patch
#         # self._gen = self._generator()
#
#     def _generator(self):
#         while True:
#             yield random.randint(self.start, self.stop)
#
#     def generator(self, count=0):
#         patch = self.patch if count <= 0 else count
#         g = self._generator()
#         return [next(g) for _ in range(patch)]
#         # return [next(self.generator()) for _ in range(self.patch)]
#         # 这种做法next(self.generator()每次都是得到第一个，不合适
#
#
# a = RandomGenerator()
# print(a.generator())
# print(a.generator(5))


# 使用生成器实现
# class RandomGenerator:
#     def __init__(self, start=1, stop=100, patch=10):
#         self.start = start
#         self.stop = stop
#         self.patch = patch
#         self._gen = self._generator()
#
#     def _generator(self):
#         while True:
#             yield random.randint(self.start, self.stop)
#
#     def generator(self, count=0):
#         patch = self.patch if count <= 0 else count
#         # g = self._generator()
#         return [next(self._gen) for _ in range(patch)]
#         # return [next(self.generator()) for _ in range(self.patch)]
#         # 这种做法next(self.generator()每次都是得到第一个，不合适
#
#
# a = RandomGenerator()
# print(a.generator())
# print(a.generator(5))


# 生成器另一种实现
# class RandomGenerator:
#     def __init__(self, start=1, stop=100, patch=10):
#         self.start = start
#         self.stop = stop
#         self.patch = patch
#         self._gen = self._generate()
#
#     def _generate(self):
#         while True:  # yield一批数据
#             yield [random.randint(self.start, self.stop) for _ in range(self.patch)]
#
#     def generate(self, count=0):
#         if count > 0:
#             self.patch = count
#         return next(self._gen)


# s = RandomGenerator()
# print(s.generate())
# print(s.generate(5))


# 使用@property
# class RandomGenerator:
#     def __init__(self, start=1, stop=100, patch=10):
#         self.start = start
#         self.stop = stop
#         self._patch = patch
#         self._gen = self._generater()
#
#     def _generater(self):
#         while True:
#             yield [random.randint(self.start, self.stop) for _ in range(self._patch)]
#
#     def generater(self):
#         return next(self._gen)
#
#     @property  # property能把方法的操作变成对属性的访问
#     def patch(self):
#         return self._patch
#
#     @patch.setter
#     def patch(self, value):
#         self._patch = value


# a = RandomGenerator()
# print(a.generater())
#
# a.patch = 5
# print(a.generater())


# 使用上题的类，随机生成20个数字，两两配对形成二维坐标系
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# points = [Point(x, y) for x, y in zip(RandomGenerator(10).generater(), RandomGenerator(10).generater())]
# for p in points:
#     print('({}:{})'.format(p.x, p.y))
#
#
# for x, y in zip(RandomGenerator(10).generater(), RandomGenerator(10).generater()):
#     points = Point(x, y)
#     print('{}:{}'.format(points.x, points.y))


# 记录车的特征，并实现增加车辆信息，显示全部车辆信息的功能
# class Car:
#     def __init__(self, mark, color, price, speed):
#         self.mark = mark
#         self.color = color
#         self.price = price
#         self.speed = speed
#
#     def get_info(self):
#         return self.__dict__
#
#     def __repr__(self):  # 字符串的表现形式，打印的是车的信息，所以在车类增加
#         return '{} {} {} {} {}'.format(type(self).__name__, self.mark[:2], self.color, self.price, self.speed)
#
#
# class AddCar:
#     # cars_info = []  # 类属性
#
#     def __init__(self):
#         self.info = []  # 实例属性
#
#     def add_car(self, car: Car):
#         self.info.append(car)
#
#     def get_info(self):
#         return self.info
#
#
# c = Car('audi', 'black', '2000$', '400km/h')
# a = AddCar()
# a.add_car(c)
# a.add_car(c)
# print(a.get_info())


# # 实现华氏温度和摄氏温度的转换
# # 思路：假定一般情况下使用摄氏度为单位，传入温度值
# # 如果不给定摄氏度，一定会把温度值转换到摄氏度
# # 为了不创建对象，就可以直接进行温度转换计算，这个类设计像个温度工具类
# class Temperature:
#     def __init__(self, t, unit='c'):
#         self._c = None
#         self._k = None
#         self._f = None
#
#         # 都要先转换到摄氏度，以后访问再计算其它单位的温度值
#         if unit.lower() == 'k':
#             self._k = t
#             self._c = self.k2c(t)
#         elif unit.lower() == 'f':
#             self._f = t
#             self._c = self.f2c(t)
#         else:
#             self._c = t
#
#     @property
#     def c(self):
#         return self._c
#
#     @property
#     def f(self):
#         if self._f is None:
#             self._f = self.c2f(self._c)  # self._f = self.c2f(self.c)
#         return self._f
#
#     @property
#     def k(self):
#         if self._k is None:
#             self._k = self.c2k(self._c)
#         return self._k
#
#     @classmethod
#     def c2f(cls, c):
#         return 9 * c / 5 + 32
#
#     @classmethod
#     def f2c(cls, f):
#         return (f - 32) * 5 / 9
#
#     @classmethod
#     def c2k(cls, c):
#         return c + 273.15
#
#     @classmethod
#     def k2c(cls, k):
#         return k - 273.15
#
#     @classmethod
#     def f2k(cls, f):
#         return cls.c2k(cls.f2c(f))
#
#     @classmethod
#     def k2f(cls, k):
#         return cls.c2f(cls.k2c(k))
#
#
# t = Temperature(0, 'f')
# print(t.c, t.k, t.f)
#
# print(Temperature.c2f(30))


# class Color:
#     RED = 0
#     BLUE = 1
#     GREEN = 2
#     GOLDEN = 3
#     BLACK = 4
#     OTHER = 1000
#
#
# class Item:
#     def __init__(self, **kwargs):
#         self.__spec = kwargs
#
#     def __repr__(self):
#         return str(sorted(self.__spec.items()))  # 字典items()排序显示
#         # return str(self.__spec)  返回字典
#
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add_items(self, item: Item):
#         self.items.append(item)
#
#     def get_items(self):
#         return self.items
#
#
# a = Cart()
# phone = Item(mark='One_plus', color=Color.BLACK, memory='8G')
# a.add_items(phone)
# print(a.get_items())


# class Item:
#     def __init__(self, price, c_type, mark, **kwargs):
#         self.price = price
#         self.type = c_type
#         self.mark = mark
#         self.__spec = kwargs
#         self.__dict__.update(kwargs)  # 动态的添加属性
#
#     def __repr__(self):
#         return '<Item {} {}>'.format(self.mark, self.color)
#
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, item: Item):
#         self.items.append(item)
#
#     def get_items(self):
#         return self.items
#
#
# a = Cart()
# phone = Item(20, '001', 'One_plus', color='BLACK', memory='8G')
# print(phone.__dict__)
# print(phone.color)
# print(phone)
#
# a.add_item(phone)
# print(a.get_items())

# l = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51]
# l1 = sorted(l)
# length = len(l1)
# print(l1)
# x = 20
# y = 40
# z = 41
# l2 = [20, 40, 41]
# while True:
#     index = length // 2
#     for i in l2:  # i=20
#         if i < l1[index]:  # 20 < 47
#             if i < l1[index//2+1]:

import bisect

# level = {'A': range(90, 101), 'B': range(80, 90), 'C': range(70, 80), 'D': range(60, 70), 'E': range(0, 60)}

# level = ['A',  'B',  'C', 'D', 'E']
# score = [[range(90, 101)], [range(80, 90)],]
# class Document:
#     def __init__(self, content):
#         self.content = content
#
#     def print(self):
#         raise NotImplementedError
#
#
# class Word(Document): pass
#
#
# def add(cls):  # 类
#     def wrapper(self):
#         print(self.content)
#     cls.print = wrapper
#     return cls
#
#
# @add  # PrintableWord = add(PrintableWord)
# class PrintableWord(Word): pass
#
#
# p = PrintableWord('test word')
# p.print()
# print(PrintableWord.__dict__)


# class Shape:
#     def get_area(self):
#         raise NotImplementedError
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_area(self):
#         p = (self.a + self.b + self.c)/2
#         s = (p * (p-self.a) * (p - self.b) * (p - self.c)) ** 0.5
#         return s
#
#
# class Rectangular(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def get_area(self):
#         s = self.length * self.width
#         return s
#
#
# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#
#     def get_area(self):
#         s = 3.14 * self.r * self.r
#         return s
#
#
# re = Rectangular(3, 4)
# print(re.get_area())

# t = Triangle(3, 4, 5)
# print(t.get_area())


# class Point:
#     def __init__(self, x, y):  # 坐标
#         self.x = x
#         self.y = y
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#     def __eq__(self, other):
#         return super().__eq__(other)
#
#
# p = Point(1, 2)
# p1 = Point(1, 2)
# print({p, p1})


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#     def __iadd__(self, other):
#         self.x, self.y = self.x + other.x, self.y + other.y
#         return self
#
#
# p1 = Point(2, 3)
# p2 = Point(2, 3)
# print(p1 + p2)


# class Item:
#     def __init__(self, price, c_type, mark, **kwargs):
#         self.price = price
#         self.type = c_type
#         self.mark = mark
#         self.__spec = kwargs
#         self.__dict__.update(kwargs)  # 动态的添加属性
#
#     def __repr__(self):
#         return '<Item {} {}>'.format(self.mark, self.color)
#
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, item: Item):
#         self.items.append(item)
#
#     def get_items(self):
#         return self.items
#
#
# a = Cart()
# phone = Item(20, '001', 'One_plus', color='BLACK', memory='8G')
# print(phone.__dict__)
# print(phone.color)
# print(phone)
#


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return '{}, {}'.format(self.x, self.y)
#
#     def __call__(self, *args, **kwargs):
#         return '<Point {}:{}>'.format(self.x, self.y)
#
#
# p = Point(4, 5)
# print(p)
# print(p())
#
#
# class Adder:
#     def __call__(self, *args):
#         ret = 0
#         for x in args:
#             ret += x
#         self.ret = ret
#         return ret
#
#
# adder = Adder()
# print(adder(4, 5, 6))
# print(adder.ret)


# def foo():
#     print()
#
#
# print(foo)
# print(foo.__dict__)
# print(foo.__call__)


# class A:
#     def __init__(self):
#         print('init')
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#
#
# # print(A())
# a = A()
# print(a())


# 定义一个斐波那契数列的类，方便调用，计算第n项
# class Fib:
#     def __init__(self):
#         self.items = [0, 1, 1]
#
#     def __call__(self, index):
#         if index < 0:
#             raise IndexError('Wrong Index')
#         elif index < len(self.items):
#             return self.items[index]
#
#         for i in range(3, index+1):
#             self.items.append(self.items[i-1] + self.items[i-2])
#         return self.items[index]
#
#
# f = Fib()
# print(f(10))


# 上例中，增加迭代的方法，返回容器的长度，支持索引的方法
# class Fib:
#     def __init__(self):
#         self.items = [0, 1, 1]
#
#     def __iter__(self):  # 返回一个新的迭代器对象
#         return iter(self.items)
#         # yield from self.items
#
#     def __len__(self):
#         return len(self.items)
#
#     def __getitem__(self, index):
#         # print('getitem')
#         return self.items[index]
#
#     def __call__(self, index):
#         if index < 0:
#             raise IndexError('Wrong Index')
#         elif index < len(self.items):
#             return self.items[index]
#
#         for i in range(3, index+1):
#             self.items.append(self.items[i-1] + self.items[i-2])
#         return self.items[index]
#
#
# f = Fib()
# print(f(10))
# print(f[6])


# class Fib:
#     def __init__(self):
#         self.items = [0, 1, 1]
#
#     def __call__(self, index):
#         return self[index]  # 调用__getitem__
#         # return self(index)  # 递归调用
#
#     def __iter__(self):
#         return iter(self.items)
#
#     def __len__(self):
#         return len(self.items)
#
#     def __getitem__(self, index):
#         if index < 0:
#             raise IndexError('Wrong Index')
#         elif index < len(self.items):
#             return self.items[index]
#         print('---------')
#         for i in range(len(self), index+1):
#             self.items.append(self.items[i-1] + self.items[i-2])
#         return self.items[index]
#
#     def __str__(self):
#         return str(self.items)
#
#
# fib = Fib()
# # print(fib(5), len(fib))
# # for x in fib:
# #     print(x)
# print(fib(10))  # 调用call, call再去调用__getitem__
# print(fib[10])  # 调用__getitem__


# class Fib:
#     def __init__(self):
#         self.items = [0, 1, 1]
#
#     def __call__(self, index):
#         if index >= len(self.items):
#             for i in range(len(self), index + 1):
#                 self.items.append(self.items[i-1] + self.items[i - 2])
#         return self.items[index]
#
#     def __getitem__(self, index):
#         return self(index)  # 调用__call__
#
#     def __len__(self):
#         return len(self.items)
#
#     def __iter__(self):
#         return iter(self.items)
#
#
# fib = Fib()
# print(fib[10])  # 调用__getitem__,再去调用__call__
# print(fib(20))  # 20 > 10,从10开始算,len(self)
#


# import time
#
#
# class Point:
#     def __init__(self):
#         print('init')
#
#     def __enter__(self):
#         print('enter')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#
#
# with Point() as f:
#     print('-'*30)
#     print(f)
#     time.sleep(2)
#     print('='*30)


# 使用装饰器显示add函数的执行时长
import time
import datetime
# from functools import wraps
#
#
# def timeit(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start = datetime.datetime.now()
#         ret = fn(*args, **kwargs)
#         delta = (datetime.datetime.now() - start).total_seconds()
#         print('{} took {}s'.format(fn.__name__, delta))
#         return ret
#     return wrapper


# @timeit
def add(x, y):
    time.sleep(1)
    return x + y


# print(add(4, 5))


# 上下文实现显示函数的执行时长
import datetime


# class Timeit:
#     def __init__(self, fn):  # fn = add
#         self.fn = fn
#
#     def __enter__(self):  # 动态添加属性
#         self.start = datetime.datetime.now()
#         print('='*30)
#         return self
#         # return self.fn  # self.fn = add
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         delta = (datetime.datetime.now() - self.start).total_seconds()
#         print('{} took {}s'.format(self.fn.__name__, delta))
#
#
# with Timeit(add) as f:
#     print('-'*30)
#     print(f.fn(4, 5))
    # print(f(4, 5))


# class Timeit:
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         print('='*30)
#         # return self.fn
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         delta = (datetime.datetime.now() - self.start).total_seconds()
#         print('took {}s'.format(delta))
#
#
# with Timeit():
#     print('-'*30)
#     print(add(4, 5))


# 当作可调用对象
# class Timeit:
#     def __init__(self, fn):  # fn = add
#         self.fn = fn
#
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         return self  # self 是实例
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         delta = (datetime.datetime.now() - self.start).total_seconds()
#         print('{} took {}s'.format(self.fn.__name__, delta))
#
#     def __call__(self, *args, **kwargs):
#         return self.fn(*args, **kwargs)
#
#
# with Timeit(add) as f:
#     print(f(4, 5))


# 把类当装饰器用
from functools import wraps, update_wrapper


class Timeit:
    def __init__(self, fn):  # fn = add
        print('init')
        # self.__doc__ = fn.__doc__
        # self.__name__ = fn.__name__
        # update_wrapper(self, fn)
        wraps(fn)(self)
        self.fn = fn

    # def __enter__(self):
    #     self.start = datetime.datetime.now()
    #     return self  # self 是实例
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     delta = (datetime.datetime.now() - self.start).total_seconds()
    #     print('{} took {}s'.format(self.fn.__name__, delta))

    def __call__(self, *args, **kwargs):
        print('call')
        start = datetime.datetime.now()
        ret = self.fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {}s'.format(self.fn.__name__, delta))
        # self.__doc__ = self.fn.__doc__  # call方法不调用就没用
        return ret


@Timeit  # add = Timeit(add) 在定义是就完成了实例化
def add(x, y):
    """This is a add function"""
    time.sleep(1)
    return x + y


print(add(4, 5))
print(add.__doc__)






































