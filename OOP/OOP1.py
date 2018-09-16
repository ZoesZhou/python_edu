# class MyClass:
#     """A excample class"""
#     x = 'abc'
#
#     def foo(self):
#         return 'My Class'
#
#
# print(MyClass.x)
# print(MyClass.foo)
# print(MyClass.__doc__)

#
# class MyClass:
#     def __init__(self):
#         print('init')
#
#
# print(1, MyClass)  # 打印类对象
# print(2, MyClass())  # 实例对象
# a = MyClass()  # 实例化


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_age(self):
#         print('{} is {}'.format(self.name, self.age))
#
#
# tom = Person('tom', 20)
# jerry = Person('jerry', 25)
# print(tom.name, jerry.age)
# jerry.age += 10
# print(jerry.age)
# jerry.show_age()


# class MyClass:
#     def __init__(self):
#         print('self in init = {}'.format(id(self)))
#
#
# c = MyClass()
# print('c = {}'.format(id(c)))

# def add_name(cls):
#     cls.NAME = name
#     return cls
#
#
# def add_name(name='tom'):
#     def wrapper(cls):
#         cls.NAME = name
#         return cls
#     return wrapper
#
#
# @add_name()
# class Person:
#     AGE = 3
#
#
# print(Person.__dict__)

# class Person:
#     def normal_method(a):
#         print('normal')
#
#
# Person.normal_method(1)
# Person().normal_method()


# class Person:
#     @classmethod
#     def class_method(cls):
#         print('class = {0.__name__}({0})'.format(cls))
#         cls.HEIGHT = 180
#
#     @staticmethod
#     def static_method():
#         print(Person.HEIGHT)
#
#
# Person.class_method()
# Person.static_method()
# print(Person.__dict__)


# class Person:
#     def __init__(self, name, age=19):
#         self.name = name
#         self.__age = age
#
#     def age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age
#
#
# tom = Person('tom')
# print(tom.age())
# tom.set_age(20)
# print(tom.age())
# print(tom.__dict__)


# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @age.deleter
#     def age(self):
#         print('del')
#
#
# tom = Person('tom')
# print(tom.age)
# tom.age = 20
# print(tom.age)
# del tom.age


import random


# class Random(object):
#     def __init__(self, batch: int, number: int, range1: int, range2: int):
#         self.__batch = batch
#         self.__number = number
#         self.__range1 = range1
#         self.__range2 = range2
#
#     # @property
#     # def get_init(self):
#     #     return self.__batch, self.__number, self.__range1, self.__range2
#
#     def get_number(self):
#         num = random.choices(range(self.__range1, self.__range2), k=self.__number)
#         return num
#
#
# s = Random(2, 20, 0, 30)
# print(s.get_number())


# class Car:
#     def __init__(self, mark='BMW', color='Black', price='2000$', speed='120km/h'):
#         self.__mark = mark
#         self.__color = color
#         self.__price = price
#         self.__speed = speed
#         self.items = [{'mark': mark, 'color': color, 'price': price, 'speed': speed}]
#
#     def add_car(self, mark, color, price, speed):
#         self.__mark = mark
#         self.__color = color
#         self.__price = price
#         self.__speed = speed
#         d = {'mark': mark, 'color': color, 'price': price, 'speed': speed}
#         self.items.append(d)
#         print("New car's mark is {},color is {},price is {},speed is {}".format(mark, color, price, speed))
#
#     def car_num(self):
#         print(self.items)
#
#
# car = Car()
# car.add_car('bmw', 'yellow', '1000$', '150km/h')
# car.car_num()


# class TempTrans:
#     def __init__(self, t: str):
#         s = ''
#         for i in t:
#             if i.isdigit():
#                 s += i
#         self.temp = int(s)
#
#     def fahrenheit(self):
#         F = 9 * self.temp / 5 + 32
#         print(F)
#
#     def celsius(self):
#         C = 5 * (self.temp - 32) / 9
#         print(C)
#
#     def kelvin_temp(self):
#         K = self.temp + 273.15
#         print(K)
#
#
# p = '12℃'
# te = TempTrans(p)
# if '℃' in p:
#     te.fahrenheit()
#     te.kelvin_temp()
# else:
#     te.celsius()


class ShoppingCar:
    def __init__(self, total=99):
        self.total = total
        self.left = total
        self.things_kind = []  # {'shoes':1}

    def add_items(self, items):  # items传入的是Things的实例
        self.left = self.left - items.number
        self.things_kind.append({'name': items.name, 'number': items.number})
        print('购物车还可以放{}件, 当前有{}件，'
              '是{}'.format(self.left, len(self.things_kind), items.name))

    def get_info(self):
        pass


class Things:
    def __init__(self, name, number):
        self.name = name
        self.number = number


sc = ShoppingCar(99)
th1 = Things('shoes', 1)
sc.add_items(th1)

th2 = Things('bed', 1)
sc.add_items(th2)




















    # @property
    # def add_car(self):
    #     return self.__mark, self.__color, self.__price, self.__speed
    #
    # @add_car.setter
    # def add_car(self, mark, color, price, speed):
    #     self.__mark = mark
    #     self.__color = color
    #     self.__price = price
    #     self.__speed = speed


























































