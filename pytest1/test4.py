# 函数注解
# def add(x: int, y: int)->int:
#     """
#
#     :param x: int
#     :param y: int
#     :return: int
#     """
#     return x + y
#
#
# # print(help(add))
# # print(add(4, 5))
# # print(add('z', '4'))
# print(add.__annotations__)

import inspect
from inspect import Parameter
from functools import wraps


def check(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)  # 拿到形参签名
        params = sig.parameters  # 拿到形参签名的有序字典
        print(params)
        values = list(params.values())  # 形参
        print(values)
        flag = False
        for index, x in enumerate(args):  # 实参(4, 5)
            param: Parameter = values[index]  # 形参
            print(param)
            if param.annotation != inspect._empty and not isinstance(x, param.annotation):
                print(x, 'not')
                # flag = True
                # break
            else:
                print(x, 'ok')
        for k, v in kwargs.items():
            param = params[k]
            if param.annotation != param.empty and not isinstance(v, param.annotation):
                print(v, 'not')
            else:
                print(v, 'ok')

        # if flag:
        #     raise TypeError
        ret = fn(*args, **kwargs)
        return ret
    print(id(wrapper))
    return wrapper


@check  # add = check(add)
def add(x: int, y: int) -> int:
    return x + y


add(4, y=5)


# # 通过签名拿到整个定义的形式，可以从中拿到参数字典（有序字典）有序字典
# # key是参数的名称，是字符串，value是参数对象，参数对象有四个属性：name,
# # default, annotation, kind, name和kind一定会有，其他的都是自定义的
# sig = inspect.signature(add)  # 拿到签名
# params = sig.parameters
# print(params)
#
#
# for i, (k, param) in enumerate(params.items()):
#     print(i, k, param)
#     print(type(param))
#     print(param.name, param.default, param.annotation, param.kind)








