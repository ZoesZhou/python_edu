# import functools
# print(1, dir())
# print(2, functools)
# print(3, functools.wraps)


# import os.path  # 导入os.path, os加入当前名词空间
# print(1, dir())  # [....., 'os']
# print(2, os)
# print(3, os.path)  # 完全限定名称访问path


# import os.path as osp  # 导入os.path并赋给osp
# print(dir())  # [......, 'osp']
# print(osp)


# from pathlib import Path, PosixPath
# print(dir())

# 在当前名词空间导入该模块所有公共成员(非下划线开头成员）或指定成员
# from pathlib import *
# print(dir())

# 加载、初始化os、os.path模块，exists加入本地名词空间并绑定
# from os.path import exists
# print(dir())


# import os
#
# print(os.path.exists)  # 同一个对象
# print(os.path.__dict__['exists'])
# print(getattr(os.path, 'exists'))


# from pathlib import Path
# print(Path, id(Path))
#
# import pathlib as pl
# print(dir())
# print(pl)
# print(pl.Path, id(pl.Path))


import sys
# print(sys.path)
for o in sys.path:
    print(o)




































