# class A:
#     x = 1
#
#     def __init__(self):
#         self.y = 5
#         self.z = 8
#
#     def show(self):
#         print(self.x, self.y, self.z)
#
#
# a = A()
# print(A.__dict__)
# print(a.__dict__)


# class A:
#     x = 1
#
#     # __slots__ = ('y', 'z')
#     # __slots__ = ['y', 'z']
#     __slots__ = 'y', 'z'
#
#     def __init__(self):
#         self.y = 5
#         self.z = 8
#
#     def show(self):
#         print(self.x, self.y, self.z)
#
#
# a = A()
# a.show()
# print(A.__dict__)
# print(a.__slots__)


# print(type(NotImplemented))
# print(type(NotImplementedError))


# class A:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         print(self, 'add')
#         # try:
#         #     x = other.x
#         # except:
#         #     x = int(other)
#         #     return self.x + x
#         # else:
#         #     return self.x + other.x
#         if hasattr(other, 'x'):
#             return self.x + other.x
#         else:
#             try:
#                 x = int(other)
#             except:
#                 x = 0
#             return self.x + x
#
#     def __iadd__(self, other):
#         print(self, 'iadd')
#         return type(self)(self.x + other.x)
#         # return type(self)(self + other)
#
#     def __radd__(self, other):
#         print(self, 'radd')
#         # return self.x + other.x
#         return self + other
#
#
# class B:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         if isinstance(other, type(self)):
#             print('b1 add-----')
#             return self.x + other.x
#         else:
#             return NotImplemented
#
#
# a = A(4)
# a1 = A(9)
# b = B(5)
# b1 = B(1)
# # print(a, b)
# # print(a + b)  # a.__add__(b)
# # print(b + a)  # a.__radd__(b)
# # print(a + a1)
# print('1' + a)


def get_id():
    start = 0
    base = None
    while True:
        if base is None:
            start += 1
        else:
            start = base + 1
        base = yield start  # 执行到yield语句函数暂停执行，等式没有赋值完成


# 第一个next在等号右边停止了，第二个next，a什么也没拿到
g = get_id()

# for _ in range(5):
#     print(next(g))

print(next(g))
print(g.send(100))  # send推动生成器执行
# for _ in range(5):
#     print(next(g))




























































