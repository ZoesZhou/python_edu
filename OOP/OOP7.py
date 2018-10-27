class A:
    def __init__(self):
        self.a1 = 'a1'
        print('A.init')

    def __get__(self, instance, owner):
        print('A.__get__{} {} {}'.format(self, instance, owner))
        # print(instance)  # 表示B的实例
        # print(owner)  # owner都是B的类
        print(self)
        # return self  # self就是A的实例
        return instance.z

    def __set__(self, instance, value):
        print('A.__set__{} {} {}'.format(self, instance, value))
        # self.data = value
        instance.z = value
        # instance.x = value  # 递归了


class B:
    x = A()
    y = 1

    def __init__(self):
        print('B.init')
        # self.x = A()  # 触发__set__
        self.x = '1'  # 触发__set__
        # self.n = A()  # 没有触发__set__


b = B()
b.x = 100
print(b.x)
