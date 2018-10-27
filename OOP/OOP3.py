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
#         # super().__init__(age)  # age=10
#         print('Cat init')
#         self.age = age + 1  # age=11
#         self.weight = weight
#         super().__init__(age)  # age=10
#
#
# c = Cat(10, 5)
# c.show()


# class Document:
#     def __init__(self, content):
#         self.content = content
#
#     def print(self): # 抽象方法
#         raise NotImplementedError
#
#
# class Word(Document): pass
#
#
# class Pdf(Document): pass


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
# class Pdf(Document): pass
#
#
# class PrintableMinix:
#     def print(self):
#         print(self.content, 'Minix')
#
#
# class PrintableWord(PrintableMinix, Word): pass
#
#
# pw = PrintableWord('test, word')
# pw.print()
# print(PrintableWord.__dict__)
# print(PrintableWord.mro())
#
#
# def add_print(cls):  # 类
#     def _print(self):
#         print(self.content, '装饰器')
#     cls.print = _print
#     return cls
#
#
# @add_print  # PrintableWord = add(PrintableWord)
# class PrintableWord(Word): pass
#
#
# pw = PrintableWord('test, word')
# pw.print()
# print(PrintableWord.__dict__)
# print(PrintableWord.mro())


class Node:
    def __init__(self, item):
        self.prev = None
        self.item = item
        self.next_t = None

    def __repr__(self):
        return '{}'.format(self.item)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = Node(item)
        if self.head is None:  # 为空，头和尾都是node
            self.head = node
            self.tail = node
        else:  # 不为空，尾巴的下个是node，尾巴的前一个是尾巴
            self.tail.next_t = node
            node.prev = self.tail
            self.tail = node  # 现在的尾巴是node

    def iter_nodes(self, reverse=False):
        current = self.head if not reverse else self.tail
        while current:
            yield current
            current = current.next_t if not reverse else current.prev

    def insert(self, index, item):
        if index < 0:
            raise IndexError
        else:
            current = None
            for i, t in enumerate(self.iter_nodes()):
                if i == index:
                    current = t
                    break
            else:
                self.append(item)
            node = Node(item)
            prev = current.prev
            next_t = current
            if prev is None:
                self.head = node
                node.next_t = next_t
                next_t.prev = node
            else:
                prev.next_t = node
                next_t.prev = node
                node.next_t = next_t
                node.prev = prev

    def pop(self):
        if self.head is None:
            raise Exception('Empty')
        node = self.tail  # 链表的尾部
        item = node.item  # 尾部的值
        prev = node.prev
        if prev is None:
            self.tail = None
            self.head = None
        else:
            prev.next_t = None
            self.tail = prev
        return item

    def remove(self, index):
        if self.tail is None:
            raise Exception('Empty')
        if index < 0:
            raise IndexError
        current = None
        for i, t in enumerate(self.iter_nodes()):
            if i == index:
                current = t
                break
        else:
            raise IndexError
        prev = current.prev
        next_t = current.next_t
        if prev is None and next_t is None:  # only one
            self.head = None
            self.tail = None
        elif prev is None:  # 头部
            self.head = next_t
            prev.next_t = None
        elif next_t is None:  # 尾部
            prev.next_t = None
            self.tail = prev
        else:
            prev.next_t = next_t
            next_t.prev = prev
        del current


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.insert(1, 3)
ll.pop()
ll.remove(1)
print(list(ll.iter_nodes()))


class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
        print('==============')


tom = Person('tom')
print(tom.age)
tom.age = 10
print(tom.age)





























