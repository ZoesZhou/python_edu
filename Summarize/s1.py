# 九九乘法表
# 1.字符串拼接
# for i in range(1, 10):
#     line = ''
#     for j in range(1, i+1):
#         product = i * j
#         if j > 1 and product < 10:
#             product = str(product) + '  '
#         else:
#             product = str(product) + ' '
#         line += str(j) + 'x' + str(i) + '=' + product
#     print(line)

# 2.format格式化字符串，向左对齐
# for i in range(1, 10):
#     for j in range(1, i+1):
#         if j == 1:
#             print('{}x{}={}'.format(j, i, i*j), end=' ')
#         else:
#             print('{}x{}={:<2}'.format(j, i, i*j), end=' ')
#     print()

# 3.format里写表达式
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={:<{}}'.format(j, i, i*j, 1 if j < 2 else 2), end=' ')
#     print()

# 从左往右斜九九乘法表
# for i in range(1, 10):
#     for j in range(i, 10):
#         print('{}x{}={:<3}'.format(i, j, i*j), end='')
#     print()

# 从右往左斜九九乘法表
# for i in range(1, 10):
#     line = ''
#     for j in range(i, 10):
#         line += '{}x{}={:<{}}'.format(i, j, i*j, 2 if j < 4 else 3)
#     print('{:>65}'.format(line))

# 打印菱形
# 1.以x轴对称，利用绝对值abs
# n = 7
# e = (n-1) // 2
# for i in range(-e, e+1):
#     i = abs(i)
#     print(' '*i + '*'*(n-2*i))

# 2.以x轴对称，采用分支
# n = 7
# e = (n-1) // 2
# for i in range(-e, e+1):
#     print(' '*(-i) + '*'*(n+2*i)) if i < 0 else print(' '*i + '*'*(n-2*i))

# 打印对顶三角形
# n = 7
# e = (n-1) // 2
# for i in range(-e, e+1):
#     i = abs(i)
#     print(' '*(3-i) + '*'*(2*i+1))

# 打印闪电
# n = 7
# e = (n-1) // 2
# for i in range(-e, e+1):
#     if i < 0:
#         print(' '*(-i) + '*'*(4+i))
#     elif i > 0:
#         print(' '*e + '*'*(4-i))
#     else:
#         print('*'*n)















































































