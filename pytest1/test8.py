# import socket
#
# line = """192.168.1.150
# 0.0.0.0
# 255.255.255.255
# 17.16.52.100
# 172.16.0.100
# 400.400.999.888
# 001.022.003.000
# 257.257.255.256"""
#
# for i, ip in enumerate(line.splitlines()):
#     print(ip)
#     try:
#         net = socket.inet_aton(ip)
#     except Exception as e:
#         print(ip, e)
#     print(i, net)
#     print(i, socket.inet_ntoa(net))


# import re
#
#
# s = """bottle\n  bag\n (big)\napple\nable"""
# for i, c in enumerate(s, 1):
#     print((i-1, c), end='\n' if i % 8 == 0 else ' ')
# print()
#
#
# regex = re.compile('[\s()]+')
# result = regex.split(s)
# print(result)

# print('-'*30)
# result = re.search('b.+', s)
# print(1, result)
#
# regex = re.compile('b.+')
# result = regex.finditer(s)
# print(6, result, type(result))
# for i in result:
#     print(i, type(i))

# print(re.sub('b\w+e', 'www', s).encode())
# regex = re.compile('b\w+e')
# result = regex.sub('www', s)
# print(result)
# regex = re.compile('b\w+e')
# result = regex.subn('www', s)
# print(result)


import json
# from configparser import ConfigParser
#
# c = ConfigParser()
# al_read = c.read('C:/test/test_1.ini')
# d = {}
# for section in c.sections():
#     print(c.items(section))
#     d[section] = dict(c.items(section))
# print(d)
# print()
# print(c.items())
# a = [('a', 1), ('b', 2)]
# s = dict(a)
# print(s)

from pathlib import Path

# p = Path('C:/test')
# print(list(p.glob('t*')))
# print(p.match('t*'))

# p1 = Path('.')
# for x in p1.iterdir():
#     print(x)
# print(p1.stat())


f = Path('C:/test/test_1.txt').open()
print(type(f))
print(f)
f.close()
