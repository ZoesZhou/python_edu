# import inspect
# from inspect import Parameter
# from functools import wraps
#
#
# def check(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters  # 形参有序字典
#         values = tuple(params.values())
#         for i, c in enumerate(args):
#             param: Parameter = values[i]
#             if param.annotation != param.empty and isinstance(c, param.annotation):
#                 print(c, 'ok')
#             else:
#                 print(c, 'wrong')
#
#         for k, v in kwargs:
#             param: Parameter = params[k]
#             if param.annotation != param.empty and isinstance(v, param.annotation):
#                 print(v, 'ok')
#             else:
#                 print(v, 'wrong')
#
#         ret = fn(*args, **kwargs)
#         return ret
#     return wrapper
#
#
# @check  # add=check(add)
# def add(x: int=4, y: int=5):
#     return x + y
#
#
# print(add(5, 5))


# def partial(func, *args, **keywords):
#     def newfunc(*fargs, **fkeywords):
#         newkeywords = fkeywords.copy()
#         newkeywords.update(fkeywords)
#         return func(*args, *fargs, **newkeywords)
#     newfunc.func = func
#     newfunc.args = args
#     newfunc.keywords = keywords
#     return newfunc


# import functools
#
#
# def add(x, y, *args):
#     print(args)
#     return x + y
#
#
# newadd = functools.partial(add, 1, 3, 6, 5)
#
#
# print(newadd(7))
# import inspect
# print(inspect.signature(newadd))

# import datetime
#
# dt = datetime.datetime(2018, 10, 5, 16, 35)
# print(dt)


# import datetime
#
# dt = datetime.datetime(2018, 10, 5, 16, 35)
# print(dt.timestamp())


# import datetime
#
# t = 1538728500.0
# print(datetime.datetime.fromtimestamp(t))
# print(datetime.datetime.utcfromtimestamp(t))


# import datetime
#
# day = datetime.datetime.strptime('2018-10-5 18:00:00', '%Y-%m-%d %H:%M:%S')
# print(day)


# import datetime
#
# now = datetime.datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))


# import datetime
# from datetime import timedelta
#
# now = datetime.datetime.now()
# print(now)
# print(now + timedelta(hours=10))


# from datetime import datetime
# from datetime import timezone
# from datetime import timedelta
#
# # 拿到UTC时间，并强制设置时区为UTC+0：00
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# # astimezone()转换为北京时区
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)


# import inspect
# from inspect import Parameter
# from functools import wraps
#
#
# def check(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters  # 形参的有序字典
#         values = tuple(params.values())
#         for i, c in enumerate(args):
#             param: Parameter = values[i]
#             if param.annotation != param.empty and isinstance(c, param.annotation):
#                 print(c, 'ok')
#             else:
#                 print(c, 'not')
#
#         for k, v in kwargs.items():
#             param: Parameter = params[k]
#             if param.annotation != param.empty and isinstance(v, param.annotation):
#                 print(v, 'ok')
#             else:
#                 print(v, 'not')
#         ret = fn(*args, **kwargs)
#         return ret
#     return wrapper
#
#
# @check
# def add(x: int=4, y: int=5):
#     return x + y
#
#
# print(add(x=4, y=5))
# print(add.__name__)
# alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
#
#
# def base64encode(src: str):
#     ret = bytearray()
#     if isinstance(src, str):
#         _src = src.encode()
#     else:
#         return
#     length = len(_src)
#     r = 0
#     for offset in range(0, length, 3):
#         triple = _src[offset:offset+3]
#         r = 3 - len(triple)
#         if r:
#             triple += b'\x00' * r
#
#         b = int.from_bytes(triple, 'big')
#         for i in range(18, -1, -6):
#             if i == 18:
#                 index = b >> i
#             else:
#                 index = b >> i & 0b111111
#             ret.append(alphabet[index])
#
#     if r:
#         ret[-r:] = b'=' * r
#     return bytes(ret)
#
#
# print(base64encode('a'))


# alphabet_t = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
# alphabet = dict(zip(alphabet_t, range(0, 64)))
#
#
# def base64decode(src: str):
#     if isinstance(src, str):
#         _src = src.encode()
#     else:
#         _src = src
#     ret = bytearray()
#     length = len(_src)
#     for offset in range(0, length, 4):
#         block = _src[offset:offset+4]
#         tmp = 0x00
#         for i in range(4):
#             index = alphabet.get(block[-i-1])
#             if index:
#                 tmp += index << i * 6
#         ret.extend(tmp.to_bytes(3, 'big'))
#     return bytes(ret.rstrip(b'\x00'))
#
#
# print(base64decode('YQ=='))
#
#
# print(bytes(range(97, 123)).decode())


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
#
#
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
#     if num[max_index] != i:
#         num[i], num[max_index] = num[max_index], num[i]
#         if min_index == i - length:
#             min_index = max_index - length
#     if num[min_index] != -i-1:
#         num[-i-1], num[min_index] = num[min_index], num[-i-1]
#
#
# print(num)


import math

print(math.ceil(1.8))
print('{:{}}'.format(30, 15))
