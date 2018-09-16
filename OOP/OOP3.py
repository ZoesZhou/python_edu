# class Animal:
#     __COUNT = 100
#     HEIGHT = 0
#
#     def __init__(self, age, weight, height):
#         self.__COUNT += 1  # 实例属性
#         self.age = age
#         self.__weight = weight
#         self.HEIGHT = height
#
#     def eat(self):
#         print('{} eat'.format(self.__class__.__name__))
#
#     def __get_weight(self):
#         print(self.__weight)
#
#     @classmethod
#     def show_count1(cls):  # 类方法
#         print(cls)
#         print(cls.__dict__)  # cls是Cat,打印Cat的字典
#         print(cls.__COUNT)  # 私有属性，show_count1在Animal中，是Animal的属性
#
#     @classmethod
#     def __show_count2(cls):  # 类方法
#         print(cls.__COUNT)  # 打印100
#
#     def show_count3(self):  # 实例方法
#         print(self.__dict__)
#         print(self.__COUNT)  # 打印101
#
#
# class Cat(Animal):
#     NAME = 'CAT'
#     __COUNT = 200
#
#
# c = Cat(3, 5, 15)
# c.eat()
# print(c.HEIGHT)
# c.show_count1()
# c.show_count3()
# print(c.NAME)
# print('='*30)
# print('{}'.format(Animal.__dict__))
# print('{}'.format(Cat.__dict__))
# print(c.__dict__)
# print(c.__class__.mro())


# class Animal:
#     def shout(self):
#         print('Animal shout')
#
#
# class Cat(Animal):
#     # 覆盖了父类的方法
#     def shout(self):
#         print('miao')
#
#     # 覆盖了自身的方法，显式调用了父类的方法
#     def shout(self):
#         print(super())
#         print(super(Cat, self))
#         super().shout()
#         super(Cat, self).shout()
#         self.__class__.__base__.shout(self)  # 不推荐
#
#
# a = Animal()
# a.shout()
# c = Cat()
# c.shout()
# print('='*30)
# print(a.__dict__)
# print(c.__dict__)
# print(Animal.__dict__)
# print(Cat.__dict__)

#
# class A:
#     def __init__(self, a, d=10):
#         self.a = a
#         self.__d = d
#
#
# class B(A):
#     def __init__(self, b, c):
#         super().__init__(b+c, b-c)
#         # A.__init__(self, b+c, b-c)  # 等价上面
#         self.b = b
#         self.c = c
#
#     def printv(self):
#         print(self.b)
#         print(self.a)
#
#
# f = B(200, 300)
# print(f.__dict__)
# print(f.__class__.__bases__)
# f.printv()


# class Animal:
#     def __init__(self, age):
#         print('Animal init')
#         self.age = age
#
#     def show(self):
#         print(self.age)
#
#
# class Cat(Animal):
#     def __init__(self, age, weight):
#         print('Cat init')
#         self.age = age + 1
#         self.weight = weight
#
#
# c = Cat(10, 5)
# c.show()


class Animal:
    def __init__(self, age):
        print('Animal init')
        self.age = age

    def show(self):
        print(self.age)


class Cat(Animal):
    def __init__(self, age, weight):
        # super().__init__(age)  # age=10
        print('Cat init')
        self.age = age + 1  # age=11
        self.weight = weight
        super().__init__(age)  # age=10


c = Cat(10, 5)
c.show()










































