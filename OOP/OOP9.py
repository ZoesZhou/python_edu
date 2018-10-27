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


# class Car:
#     def __init__(self, mark, color, price, speed):
#         self.mark = mark
#         self.color = color
#         self.price = price
#         self.__speed = speed
#
#     def get_info(self):
#         return list(filter(lambda x: x[0].isalpha(), self.__dict__))
#
#     def __repr__(self):
#         return '{} {} {} {} {}'.format(type(self).__name__, self.mark, self.color, self.price, self.__speed)
#
#
# class CarInfo:
#     def __init__(self):
#         self.info = []
#
#     def add_car(self, car: Car):
#         self.info.append(car)
#
#     def get_all(self):
#         return self.info
#
#
# ci = CarInfo()
# car = Car('audi', 400, 'red', 100)
# print(car.get_info)
# ci.add_car(car)
# print(ci.get_all())

# 实现华氏温度和摄氏温度的转换
# 思路：假定一般情况下使用摄氏度为单位，传入温度值
# 如果不给定摄氏度，一定会把温度值转换到摄氏度
# 为了不创建对象，就可以直接进行温度转换计算，这个类设计像个温度工具类

# class Temperature:
#     def __init__(self, t, unit='c'):
#         self._c = None
#         self._f = None
#         self._k = None
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
#             self._f = self.c2f(self._c)
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
#     def c2k(cls, c):
#         return c + 273.15
#
#     @classmethod
#     def k2c(cls, k):
#         return k - 273.15
#
#     @classmethod
#     def f2c(cls, f):
#         return (f - 32) * 5 / 9
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
# t = Temperature(20, 'c')
# print(t.c, t.k, t.f)
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
#         return str(sorted(self.__spec.items()))
#
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, item):
#         self.items.append(item)
#
#     def get_item(self):
#         return self.items
#
#
# c = Cart()
# my = Item(mark='se', color=Color.BLACK, speed=90)
# c.add_item(my)
# print(c.get_item())


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return str(self.data)
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, item):
#         node = Node(item)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#
#     def iter_nodes(self):
#         current = self.head
#         while current:
#             yield current
#             current = current.next
#
#
# ll = LinkedList()
# ll.append(1)
# ll.append(8)
# ll.append(9)
# for item in ll.iter_nodes():
#     print(item)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def iter_nodes(self, reverse=False):
        current = self.head if not reverse else self.tail
        while current:
            yield current
            current = current.next if not reverse else current.prev

    def pop(self):
        if self.tail is None:
            raise Exception('Empty')
        node = self.tail
        if self.tail.prev is None:  # 只有一个
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail.prev = self.tail
        return node.data

    def insert(self, index, data):
        if index < 0:
            raise IndexError
        current = None
        for i, c in enumerate(self.iter_nodes()):
            if i == index:
                current = c
                break
        else:  # 没有找到
            self.append(data)
            return

        node = Node(data)
        if current.prev is None:  # index = 0
            self.head = node
            node.next = current
            current.prev = node
        else:
            current.prev = node
            current.prev.next = node
            node.next = current
            node.prev = current.prev

    def remove(self, index):
        if self.tail is None:
            raise Exception('Empty')
        if index < 0:
            raise IndexError
        current = None
        for i, c in enumerate(self.iter_nodes()):
            if i == index:
                current = c
                break
        else:
            raise IndexError

        if current.next and current.prev is None:  # 只有一个
            self.head = None
            self.tail = None
        elif current.prev is None:
            self.head = current.next
            current.next.prev = None
        elif current.next is None:
            self.tail = current.prev
            current.prev.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        del current


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
for i in ll.iter_nodes():
    print(i)
ll.pop()
for i in ll.iter_nodes():
    print(i)
ll.remove(1)
for i in ll.iter_nodes():
    print(i)
ll.insert(0, 4)
for i in ll.iter_nodes():
    print(i)















































































