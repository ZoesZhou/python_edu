# from configparser import ConfigParser
#
# c = ConfigParser()
# readok = c.read('C:\\test\\test_1.ini')
# print(readok)
#
# print(c.sections())


# from configparser import ConfigParser
# import json
# OrderedDict = {}
# c = ConfigParser()
# read_ok = c.read('C:/test/test_1.ini')
#
# OrderedDict['DEFAULT'] = {'a': 'test'}
# for section in c.sections():
#     OrderedDict[section] = dict()  # 创建空字典
#     for option in c.options(section):
#         v = c.get(section, option)
#         OrderedDict[section].update({option:v})
#
# print(OrderedDict)

# with open('C:/test/test_json.txt', 'w') as f:
#     j = json.dump(OrderedDict, f)


import argparse



# print(list(map(str.lower, ['A', 'B', 'C'])))


# 分割key的另一种思路
s = 'os.path'
def make_key1(s: str):  # '..a '   'd..'
    chars = set(r"""!,.`#/\(){}[]*-_——""")
    key = s.lower()
    ret = []
    # start = 0
    length = len(key)
    for i, c in enumerate(key):
        start = 0
        if c in chars:  #i=2,6
            if start == i:
                start += 1
                continue
            ret.append(key[start:i])  # s[0,2]
            start = i + 1
    else:
        if start < length:
            ret.append(key[start:])
    print(ret)


make_key1(s)