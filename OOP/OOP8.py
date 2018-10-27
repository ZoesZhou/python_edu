# def foo():
#     print('before')
#
#     def bar():
#         print(1/0)
#
#     bar()
#     print('after')
#
#
# foo()


# try:
#     print('begin')
#     c = 1 / 0
#     print('end')
# except:
#     print('catch the exception')
# print('outer')


# try:
#     print('begin')
#     c = 1 / 0
#     print('end')
# except ArithmeticError:
#     print('catch the ArithmeticError')
# print('outer')


import sys

# print('before')
# sys.exit(0)
# print('SysExit')
# print('outer')


# try:
#     sys.exit(1)
# except SystemExit:
#     print('SysExit')
# print('outer')
#


# try:
#     import time
#     while True:
#         time.sleep(1)
#         pass
# except KeyboardInterrupt:
#     print('ctl + c')
# print('outer')


# f = None
# try:
#     f = open('ee')
# except Exception as e:
#     print('{}'.format(e))
# finally:
#     print('clean')
#     if f:
#         f.close()


# try:
#     f = open('rw')
# except Exception as e:
#     print('{}'.format(e))
# finally:
#     print('clean')
#     try:
#         f.close()
#     except NameError as e:
#         print(e)


# import threading
# import time
#
#
# def foo1():
#     return 1 / 0
#
#
# def foo2():
#     time.sleep(3)
#     print('foo2 start')
#     foo1()
#     print('foo2 stop')
#
#
# t = threading.Thread(target=foo2)
# t.start()
#
# while True:
#     time.sleep(1)
#     print("it's ok")
#     if t.is_alive():
#         print('alive')
#     else:
#         print('dead')


import random


# class RandomGen:
#     def __init__(self, start=1, stop=100, patch=10):
#         self.start = start
#         self.stop = stop
#         self.patch = patch
#
#     # def get_number(self):
#     #     return [random.randint(self.start, self.stop) for _ in range(self.patch)]
#
#     def _generator(self):
#         while True:
#             yield random.randint(self.start, self.stop)
#
#     def generator(self, count=0):
#         if count:
#             self.patch = count
#         g = self._generator()
#         return [next(g) for _ in range(self.patch)]
#
#     def __call__(self, count):
#         return self.generator(count)
#
#
# rg = RandomGen()
# # print(rg.get_number())
# # print(rg.generator(5))
# print(rg(5))


# class RandomGen:
#     def __init__(self, start=1, stop=100, patch=10):
#         self.start = start
#         self.stop = stop
#         self.patch = patch
#         self.gen = self._generator()
#
#     # def _generator(self):
#     #     while True:
#     #         yield random.randint(self.start, self.stop)
#
#     def _generator(self):
#         while True:
#             yield [random.randint(self.start, self.stop) for _ in range(self.patch)]
#
#     def generator(self, count=0):
#         if count:
#             self.patch = count
#         # self.gen = self._generator()
#         # return [next(self.gen) for _ in range(self.patch)]
#         return next(self.gen)
#
#
# rg = RandomGen()
# print(rg.generator())
# print(rg.generator(5))


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
#         return [next(self._gen) for _ in range(patch)]
#
#
# rg = RandomGenerator()
# print(rg.generator())
# print(rg.generator(2))


# 使用@property
# class RandomGen:
#     def __init__(self, start=1, stop=100, patch=10):
#         self.start = start
#         self.stop = stop
#         self.__patch = patch
#         self._gen = self._generator()
#
#     def _generator(self):
#         while True:
#             yield [random.randint(self.start, self.stop) for _ in range(self.__patch)]
#
#     def generator(self):
#         return next(self._gen)
#
#     @property
#     def patch(self):
#         return self.__patch
#
#     @patch.setter
#     def patch(self, value):
#         self.__patch = value
#
#
# rg = RandomGen()
# print(rg.generator())
# rg.patch = 10
# print(rg.generator())
# print(rg.generator())
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def point(self):
#         return self.x, self.y
#
#
# for x, y in zip(rg.generator(), rg.generator()):
#     points = Point(x, y)
#     print(points.point())
# print('------------------')
# points = [Point(x, y) for x, y in zip(rg.generator(), rg.generator())]
# for p in points:
#     print(p.point())


class Car:
    def __init__(self, mark, color, price, speed):
        self.mark = mark
        self.color = color
        self.price = price
        self.__speed = speed

    def get_info(self):
        return list(filter(lambda x: x[0].isalpha(), self.__dict__))

    def __repr__(self):
        return '{} {} {} {} {}'.format(type(self).__name__, self.mark, self.color, self.price, self.__speed)


class CarInfo:
    def __init__(self):
        self.info = []

    def add_car(self, car: Car):
        self.info.append(car)

    def get_all(self):
        return self.info


ci = CarInfo()
car = Car('audi', 400, 'red', 100)
print(car.get_info)
ci.add_car(car)
print(ci.get_all())































