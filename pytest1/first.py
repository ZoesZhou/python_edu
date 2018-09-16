# a = input(">>")
# a = int(a)
# b = input('>>')
# b = int(b)
# if a > b:
#     print(a)
# else:
#     print(b)

# b = 1
# i = 1
# a = 0
# while True:
#     a, b = b, a+b
#     i += 1
#     if i == 101:
#         print(b)
#         break

# b = 1
# i = 1
# a = 0
# for i in range(1, 101):
#     a, b = b, a+b
#     print(b)
# a = input('>>')

# if a == ' ':
#     print(3)


# n = 100
# count = 2
# for num in range(4, n):
#     if num % 6 != 1 and num % 6 != 5:
#         continue
#     else:
#         snum = int(num**0.5+1)
#         for i in range(3, snum, 2):
#             if not num % i:
#                 break
#         else:
#             count += 1
#             print(num, end=' ')


# L = [2]
# for i in range(3, 100, 2):
#     for j in range(3, int(i**0.5)+1, 2):
#         if not i % j:
#             break
#     else:
#         L.append(i)
# print(L)


# l = [2, 3]
# n = 100
# count = 2
# step = 2
# x = 5
# while x <= n:
#     for i in range(3, int(x**0.5)+1, 2):
#         if not x % i:
#             break
#     else:
#         count += 1
#     x += step
#     if step == 2:
#         step = 4
#     else:
#         step = 2
# print(count)


# 冒泡排序
# L = [1, 2, 3, 4, 5, 6, 7, 9, 8]
# length = len(L)
# count = 0
# count_ch = 0
# for i in range(length-1):
#     flag = False
#     for j in range(length-1-i):
#         count += 1
#         if L[j] > L[j+1]:
#             temp = L[j]
#             L[j] = L[j+1]
#             L[j+1] = temp
#             count_ch += 1
#             flag = True
#     if not flag:
#         break
# print(L)
# print(count)
# print(count_ch)


# 杨辉三角单行列表写法
# n = 6
# row = [1] * n
#
# for i in range(n):
#     offset = n - i
#     z = 1  # 因为会有覆盖影响计算，引入一个临时变量
#     for j in range(1, i//2+1):
#         val = z + row[j]
#         z = row[j]
#         row[j] = val
#         if i != 2 * j:
#             row[-j-offset] = val
#     print(row[:i+1])

# num = '00121055'.lstrip('0')
# length = len(num)
# counter = [0] * 10 # 创建一个0-9的列表用来存储num里出现的数字的次数
# for x in num: #计算num里数字出现的次数
#     i = int(x)
#     counter[i] = counter[i] + 1
#
# for i in range(len(counter)):
#     if counter[i]:
#         print('The count of {} is {}'.format(i, counter[i]))


# num = [11, 7, 5, 11, 6, 7, 4]
# length = len(num)
# states = [0] * length
# samenums = []
# diffnums = []
# for i in range(length): #i=0
# #     if states[i] == 1:
# #         continue
#     flag = False
#     for j in range(i+1,length): #j=1
#         # if states[j] == 1:
#         #     continue
#         if num[i] == num[j]:
#             states[j] = 1
#             flag = True
#     if flag:
#         states[i] = 1
#         samenums.append(num[i])
#     else:
#         diffnums.append(num[i])
# print(samenums)
# print(diffnums)
# print(states)
# print('重复的数字有{}个, 是{}'.format(len(samenums), samenums))
# print('不重复的数字有{}个, 是{}'.format(len(diffnums), diffnums))

# m = 6
# k = 2
# oldline = [] # 新旧两行一次开辟
# for i in range(m): #i=2
#     newline = [1] * (i+1)
#     for j in range(i-1):
#         newline[j+1] = oldline[j] + oldline[j+1]
#     oldline = newline
#     print(newline)


# n = 100
# l = [2]
# for i in range(3, n, 2):
#     if i % 6 == 1 and i % 6 == 5:
#         continue
#     edge = int(i**0.5)
#     for j in l:
#         if i % j ==0:
#             break
#         if j > edge:
#             break
#
#     l.append(i)
# print(l)

# n = 100
# l = [2, 3]
# x = 5
# step = 2
# while x < n:
#     flag = False
#     edge = int(x ** 0.5)
#     for j in l:
#         if x % j == 0:
#             flag = True
#             break
#         if j > edge:
#             break
#     if not flag:
#         l.append(x)
#     x += step
#     step = 4 if step == 2 else 2
# print(l)


# n = 6
# triangle = []
# for i in range(n):
#     cur = [1]
#     triangle.append(cur)
#     if i == 0:
#         continue
#     pre = triangle[i-1]
# # print(triangle)
#     for j in range(i-1):
#         cur.append(pre[j] + pre[j+1])
#     cur.append(1)
# print(triangle)

# n = 6
# newline = [1]
# print(newline)
#
# for i in range(1, n):
#     oldline = newline.copy()
#     oldline.append(0)
#     newline.clear()
#
#     for j in range(i + 1):
#         newline.append(oldline[j - 1] + oldline[j])
#     print(newline)
#

# num = '64432230'
# counter = {}
# for i in num:
#     counter[i] = counter.get(i, 0) + 1
# print(counter.items())

# num = [1, 9, 8, 5, 6, 7, 4, 3, 2]
# length = len(num)
# for i in range(length): #i=0
#     maxindex = i
#     for j in range(i+1, length): #j=1-8
#         if num[j] > num[maxindex]:
#             maxindex = j
#     num[i], num[maxindex] = num[maxindex], num[i]
# print(num)


# num = [1, 9, 8, 5, 6, 7, 4, 3, 2]
# length = len(num)
# count = 0
# count_swap = 0
# for i in range(length // 2):
#     maxindex = i
#     minindex = -i - 1
#     for j in range(i + 1, length-i):
#         count += 1
#         if num[j] > num[maxindex]:
#             maxindex = j
#         if num[-j - 1] < num[minindex]:
#             minindex = -j - 1
#     if i != maxindex:
#         num[i], num[maxindex] = num[maxindex], num[i]
#         count_swap += 1
#         if minindex == i - length:
#             minindex = maxindex - length
#     if -i - 1 != minindex:
#         num[-i - 1], num[minindex] = num[minindex], num[-i - 1]
#         count_swap += 1
# print(num)
# print(count, count_swap)


# n = 4
# triangle = [1] * n
# for i in range(n):
#     for j in range(i//2):
#         val = triangle[j] + triangle[j+1]
#         triangle[j+1] = val
#         if i != 2 * j:
#             triangle[-j-2] = val
#     print(triangle[:i+1])


n = 6
row = [1] * n
for i in range(n):
    offset = n - i
    z = 1
    for j in range(1, i//2+1):
        val = z + row[j]
        z = row[j]
        row[j] = val
        if i != 2 * j:
            row[-j-offset] = val
    print(row[:i+1])