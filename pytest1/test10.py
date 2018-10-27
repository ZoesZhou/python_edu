# def fib(n):
#     return 1 if n < 3 else fib(n-1) + fib(n-2)
#
#
# print(fib(5))
#
#
# def fib(n, a=0, b=1):  # n=3
#     if n < 3:
#         return a + b  # 2
#     else:
#         a, b = b, a + b  # a, b=1, 1
#         return fib(n-1, a, b)  # fib(2, 1, 1)
#
#
# print(fib(10))
#
#
# def fib(n, a=0, b=1):
#     a, b = b, a + b  # a=1, b=1
#     if n < 3:
#         return b
#     else:
#         return fib(n-1, a, b)
#
#
# print(fib(10))


# def factorial(n):
#     if n < 2:
#         return 1
#     return factorial(n-1) * n
#
#
# print(factorial(3))
#
#
# def factorial(n, product=1):  # n=3
#     product = product * n  # 1*3
#     if n < 2:
#         return product
#     return factorial(n-1, product)  # factorial(2, 3)
#
#
# print(factorial(4))
# print(60 & 13)


# 将1234逆序放入列表中[4321]
# data = str(1234)
#
#
# def revert(x, target=[]):  # x=2
#     if x == -1:  # x=-4
#         return target
#     target.append(data[x])
#     return revert(x-1)
#
#
# print(revert(len(data)-1))


data = str(1234)


# def revert(n):  # n=3
#     if n == -1:
#         return []
#     return [data[n]] + revert(n-1)  # [4]+revert(2),[3]+revert(1)
# # [2]+revert(0)
#
#
# print(revert(len(data)-1))
#
#
# data = str(1234)
#
#
# def revert(x, target=[]):
#     if x:
#         target.append(x[-1])
#         revert(x[:-1])
#     return target
#
#
# print(revert(data))
#
#
# def peach(days=10):
#     if days == 1:
#         return 1
#     return (peach(days-1) + 1) * 2
#
#
# print(peach())
#
#
# def peach(n=9, x=1):
#     for i in range(n):
#         x = (x + 1) * 2
#     return x
#
#
# print(peach())
# import inspect
# from inspect import Parameter
# from functools import wraps
#
#
# def check(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)  # 拿到函数括号内的元素
#         params = sig.parameters  # 拿到函数括号内形参的有序字典
#         print(params)
#         values = tuple(params.values())  # (x:int, y:int=7)
#         print(values)
#         for i, c in enumerate(args):
#             param: Parameter = values[i]
#             print(param, 1)
#             if param.annotation != param.empty and isinstance(c, param.annotation):
#                 print(c, 'ok')
#                 print(param.annotation)
#             else:
#                 print(c, 'not')
#
#         for k, v in kwargs.items():
#             param: Parameter = params[k]
#             if param.annotation != param.empty and isinstance(v, param.annotation):
#                 print(v, 'ok')
#             else:
#                 print(v, 'not')
#
#         ret = fn(*args, **kwargs)
#         return ret
#     return wrapper
#
#
# @check
# def add(x: int, y: int=7):
#     return x + y
#
#
# print(add(4, 5))
# print(add.__annotations__)


# base64编码
# alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
#
#
# def base64encode(data: str):
#     ret = bytearray()
#     if isinstance(data, str):
#         _data = data.encode()
#     else:
#         return
#     length = len(_data)
#     r = 0
#     for offset in range(0, length, 3):
#         triple = _data[offset:offset+3]
#         if offset + 3 > length:
#             r = 3 - len(triple)
#             triple += b'\x00' * r
#         b = int.from_bytes(triple, 'big')
#         # print(b)
#         for i in range(18, -1, -6):
#             if i == 18:
#                 index = b >> i
#             else:
#                 index = b >> i & 0x3F
#             ret.append(alphabet[index])
#             # print(ret)
#
#     if r:
#         ret[-r:] = b'=' * r
#     return bytes(ret)
#
#
# print(base64encode('a'))
# print(base64encode('abc'))


# alphabet_t = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
# alphabet = dict(zip(alphabet_t, range(64)))
#
#
# def base64decode(src: str):
#     ret = bytearray()
#     if isinstance(src, str):
#         _src = src.encode()
#     else:
#         _src = src
#     length = len(_src)
#     for offset in range(0, length, 4):
#         strip = _src[offset:offset+4]
#         tmp = 0x00
#
#         for i in range(0, 4):
#             index = alphabet.get(strip[-i-1])
#             if index is not None:
#                 tmp += index << 6 * i
#         ret.extend(tmp.to_bytes(3, 'big'))
#     return bytes(ret.strip(b'\x00'))
#
#
# print(base64decode('YQ=='))


# 冒泡排序
# lst = [1, 9, 8, 5, 6, 7, 4, 3, 2]
# length = len(lst)
# for i in range(length-1):
#     flag = False
#     for j in range(length-1-i):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#             flag = True
#     if not flag:
#         break
#
# print(lst)

# 选择排序
# num = [1, 9, 8, 5, 6, 7, 4, 3, 2]
# length = len(num)
# for i in range(length):
#     max_index = i
#     for j in range(i+1, length):
#         if num[j] > num[max_index]:
#             max_index = j
#     if max_index != i:
#         num[i], num[max_index] = num[max_index], num[i]
#
# print(num)


# num = [1, 9, 8, 5, 6, 7, 4, 3, 2]
# length = len(num)
# for i in range(length//2):
#     max_index = i
#     min_index = -i-1
#     for j in range(i+1, length-i):
#         if num[j] > num[max_index]:
#             max_index = j
#         if num[-j-1] < num[min_index]:
#             min_index = -j-1
#     if num[max_index] == num[min_index]:
#         break
#     if max_index != i:
#         num[i], num[max_index] = num[max_index], num[i]
#         if min_index == i - length:
#             min_index = max_index - length
#     if min_index != -i-1:
#         num[-i-1], num[min_index] = num[min_index], num[-i-1]
#
#
# print(num)


# 直接插入排序
# origin = [1, 9, 8, 5, 6, 7, 4, 3, 2]
# nums = [0] + origin
# length = len(nums)
# for i in range(2, length):  # i=3
#     nums[0] = nums[i]  # num[3]=8
#     j = i - 1  # j=2,num[2]=9
#     if nums[j] > nums[0]:
#         while nums[j] > nums[0]:
#             nums[j+1] = nums[j]
#             j -= 1
#         nums[j+1] = nums[0]
#
# print(nums[1:])
#
#
# origin = [1, 9, 8, 5, 6, 7, 4, 3, 2]
# num = [0] + origin
# length = (len(num))
# for i in range(2, length):  # i=3
#     num[0] = num[i]
#     j = i - 1  # j=2
#     if num[j] > num[0]:
#         while num[j] > num[0]:
#             num[j+1] = num[j]
#             j -= 1
#         num[j+1] = num[0]
#
# print(num[1:])


# 打印树
# import math
#
#
# def print_tree(array, unit_width=2):
#     length = len(array)  # 9
#     depth = math.ceil(math.log2(length))  # 4
#     index = 0
#     width = 2 ** depth - 1  # 行宽，最深的行15个数
#     for i in range(depth):  # 0,1,2,3
#         for j in range(2 ** i):  # i=0:0,i=1:0,1
#             print('{:^{}}'.format(array[index], width * unit_width), end=' ' * unit_width)
#             index += 1
#             if index >= length:
#                 break
#         width = width // 2
#         print()
#
#
# print_tree([x+1 for x in range(9)])











































































