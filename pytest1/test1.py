import datetime
# start = datetime.datetime.now()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a + b + c == 1000 and a**2 + b**2 == c**2:
#                 print('a', 'b', 'c', '{ },{},{}'.format(a, b, c))
# print((datetime.datetime.now()-start).total_seconds())

# start = datetime.datetime.now()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         c = 1000 - a - b
#         if a**2 + b**2 == c**2:
#             print('a,', 'b,', 'c:', '{},{},{}'.format(a, b, c))
# print((datetime.datetime.now()-start).total_seconds())

# a = input('first:')
# while True:
#     b = input('second:')
#     if a == '' and b == '':
#         break
#     else:
#         a = int(a)
#         b = int(b)
#         if b > a:
#             a = b
#         print(a)

# s = 0
# i = 0
# while True:
#     a = input('>>')
#     i += 1
#     if a == 'q':
#         break
#     else:
#         a = int(a)
#         s += a
#         average = s / i
#         print(average)


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={:<{}}'.format(j, i, i*j, 2 if j == 1 else 3), end='')
#     print()


# for i in range(1, 10):
#     s = ''
#     for j in range(i, 10):
#         s += '{}x{}={:<{}}'.format(i, j, i*j, 2 if j < 4 else 3)
#     print('{:>65}'.format(s))


# l = [1, 9, 8, 5, 6, 7, 4, 3, 2]
# # l = [3, 1, 2]
# length = len(l)
# for i in range(length-1):  # range(0, 2) -> 0, 1
#     for j in range(length-1-i):  # range(0, 1)
#         if l[j] > l[j+1]:
#             temp = l[j]
#             l[j] = l[j+1]
#             l[j+1] = temp
# print(l)


# L = []
# for i in range(5):  # 0 -4
#     if i == 0:
#         L.append(1)
#     if i == 1:
#         L.append(1)
#     for j in range(i-1):  #
#         L.insert(j+1, L[j] + L[j+1])
#     print(L)

# def angles(n):
#     l = [[1]]
#     # 列表l有n个子列表，切记不可通过l=[[1]]*n实现
#     for i in range(n):
#         l.append([1])
#     # 从l[1]开始
#     for i in range(1, n):
#         for x in range(1, i):
#             l[i].append(l[i-1][x-1]+l[i-1][x])
#         l[i].append(1)
#     for i in range(n):
#         print(l[i])
#
#
# angles(5)


# l = [1, 2, 3, 4, 5, 6, 7, 9, 8]
# length = len(l)
# count = 0
# count_ch = 0
# for i in range(length-1):
#     flag = False
#     for j in range(length-1-i):
#         count += 1
#         if l[j] > l[j+1]:
#             temp = l[j]
#             l[j] = l[j+1]
#             l[j+1] = temp
#             count_ch += 1
#             flag = True
#     if not flag:
#         break
# print(l, count, count_ch)


# a = 1
# s = 0
# for i in range(1, 6):
#     a *= i
#     s += a
# print(a)
# print(s)

# l = [2]
# count = 1
# n = 100
# for i in range(3, n, 2):
#     flag = False
#     for j in l:
#         if i % j == 0:
#             flag = True
#             break  #  合数
#         if j > i**0.5:
#             break  # 质数
#     if not flag:
#         count += 1
#         l.append(i)
# print(count)
# print(l)


n = 6
row = [1] * n
for i in range(n):
    offset = n - i
    z = 1 #因为会有覆盖计算，所以引入一个临时变量
    for j in range(1, i//2+1): # 对称性
        val = z + row[j]
        z = row[j]
        row[j] = val
        if i != 2 * j:
            row[-j-offset] = val
    a = row[:i+1]
    print(a)