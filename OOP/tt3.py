# import m
import m.m1
# from m import m1
# from m.m2 import m21
# import m.m2.m21
import sys
import os.path
# print('-'*30)
# print(1, dir())
# print(2, dir(m))
# print(3, m.m1)
# print(4, sorted(filter(lambda x: x.startswith('m'), sys.modules)))
print(__file__)  # 当前模块文件
print(os.path.dirname(__file__))  # 当前模块运行路径
