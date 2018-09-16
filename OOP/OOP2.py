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


class Item:
    def __init__(self, price, c_type, mark, **kwargs):
        self.price = price
        self.type = c_type
        self.mark = mark
        self.__spec = kwargs
        self.__dict__.update(kwargs)  # 动态的添加属性

    def __repr__(self):
        return '<Item {} {}>'.format(self.mark, self.color)


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def get_items(self):
        return self.items


a = Cart()
phone = Item(20, '001', 'One_plus', color='BLACK', memory='8G')
print(phone.__dict__)
print(phone.color)
print(phone)

a.add_item(phone)
print(a.get_items())




















































































