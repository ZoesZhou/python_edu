# n = 12
# for i in range(1, n+1):
#     for j in range(n, 0, -1):
#         if i < j:
#             print(' '*len(str(j)), end=' ')
#         else:
#             print(j, end=' ')
#     print()
#


# def triangle(n):
#     tail = ' '.join(str(i) for i in range(n, 0, -1))
#     length = len(tail)
#     print(tail)
#     for i in range(length):
#         if tail[i] == ' ':
#             print(' '*i, tail[i+1:])
#
# triangle(12)


# def triangle(n):
#     tail = ' '.join(str(i) for i in range(n, 0, -1))
#     print(tail)
#     length = len(tail)
#     point = {10 ** i for i in range(1, 3)}
#     start = 3
#     step = 3
#     for i in range(n):
#         print('{:>{}}'.format(tail[start:], length))
#         if i + 1 in point:
#             step -= 1
#         start += step
#
#
# triangle(12)

# origin = [1, 9, 8, 5, 6]
# nums = [0] + origin
# length = len(nums)
# for i in range(2, length):  # i=3
#     nums[0] = nums[i]
#     j = i - 1
#     if nums[j] > nums[0]:
#         while nums[j] > nums[0]:
#             nums[j + 1] = nums[j]
#             j -= 1
#         nums[j + 1] = nums[0]
# print(nums)


# num = [1, 6, 9, 2, 7, 5, 4, 8, 0, 3]
# length = len(num)
# for i in range(length):
#     flag = False
#     for j in range(length-1-i):
#         if num[j] > num[j+1]:
#             num[j], num[j+1] = num[j+1], num[j]
#             flag = True
#     if not flag:
#         break
#
# print(num)


# num = [1, 6, 9, 2, 7, 5, 4, 8, 0, 3]
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

# num = [1, 6, 9, 2, 7, 5, 4, 8, 0, 3]
# length = len(num)
# for i in range(length//2):
#     max_index = i
#     min_index = -i-1
#     for j in range(i+1, length-i):
#         if num[j] > num[max_index]:
#             max_index = j
#         if num[-j-1] < num[min_index]:
#             min_index = -j-1
#     if max_index != i:
#         num[i], num[max_index] = num[max_index], num[i]
#         if min_index == i - length:
#             min_index = max_index - length
#     if min_index != -i-1:
#         num[-i-1], num[min_index] = num[min_index], num[-i-1]
#
# print(num)


# origin = [1, 6, 9, 2, 7, 5, 4, 8, 0, 3]
# num = [0] + origin
# length = len(num)
# for i in range(2, length):
#     num[0] = num[i]
#     j = i-1
#     if num[j] > num[0]:
#         while num[j] > num[0]:
#             num[j+1] = num[j]
#             j -= 1
#         num[j+1] = num[0]
#
# print(num[1:])


# def counter():
#     c = [0]
#     def inc():
#         c[0] += 1
#         return c[0]
#     return inc
#
# foo = counter()
# print(foo(), foo())




# def counter():
#     c = 0
#     def inc():
#         nonlocal c
#         c += 1
#         return c
#     return inc
#
# foo = counter() # foo=inc
# print(foo(), foo())
# c = 100
# print(foo())





# def logger(fn):
#     def wrapper(*args, **kwargs):
#         """This is a function of wrapper"""
#         print('begin')
#         x = fn(*args, **kwargs)
#         print('end')
#         return x
#     return wrapper
#
# @logger #等价于add = logger(add)  ->add 就是wrapper
# def add(x, y):
#     """This is a function of add"""
#     return x + y
#
# add=logger(add)
# print(add(4, 5))

