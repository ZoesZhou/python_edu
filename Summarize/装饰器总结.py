# 使用装饰器显示add函数的执行时长
import time
import datetime
from functools import wraps


def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {}s'.format(fn.__name__, delta))
        return ret
    return wrapper
#
#
# @timeit
# def add(x, y):
#     time.sleep(1)
#     return x + y
#
#
# print(add(4, 5))


# 把类当装饰器用
from functools import wraps, update_wrapper


class Timeit:
    def __init__(self, fn):  # fn = add
        print('init')
        # self.__doc__ = fn.__doc__
        # self.__name__ = fn.__name__
        # update_wrapper(self, fn)
        wraps(fn)(self)
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print('call')
        start = datetime.datetime.now()
        ret = self.fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {}s'.format(self.fn.__name__, delta))
        return ret


@Timeit  # add = Timeit(add)  # 看似用的是类，但实际上用的是实例
# @timeit
def add(x, y):  # 因为有__call__，所以类才能当装饰器用
    """This is a add function"""
    time.sleep(1)
    return x + y


print(add(4, 5))
print(add.__doc__)
# print(callable(Timeit))  # 类是一个可调用对象
# print(callable(Timeit(add)))  #
#
# import inspect
# print(inspect.signature(Timeit), '----')


# 用类装饰器从__init__()获取参数类型，来把实例属性变成描述器
class TypeCheck:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.data = {}

    def __get__(self, instance, owner):
        print('get')
        if instance is not None:
            return instance.__dict__[self.name]
            # return self.data[self.name]
            # return getattr(self, self.name)  # 报错
        return self  # return和break作用等同

    def __set__(self, instance, value):  # instance=Person的实例
        print('set')
        if not isinstance(value, self.kind):
            raise TypeError
        instance.__dict__[self.name] = value
        # self.data[self.name] = value
        # setattr(self, self.name, value)  # 报错
        # 产生递归，相当于self.name=value,又会触发__get__
        # setattr(instance, self.name, value)  # 不能这么写


import inspect


class TypeAssert:
    def __init__(self, cls):
        self.cls = cls
        sig = inspect.signature(cls)
        params = sig.parameters  # params是有序字典
        for name, param in params.items():
            if param.annotation != param.empty:
                setattr(cls, name, TypeCheck(name, param.annotation))

    def __call__(self, name, age):
        return self.cls(name, age)


@TypeAssert  # Person=TypeAssert(Person)
class Person:
    # name = TypeCheck('name', str)  # 构成描述器
    # age = TypeCheck('age', int)

    def __init__(self, name: str, age: int):
        self.name = name  # 触发__set__
        self.age = age


# Person实例化的时候,self.name,self.age触发__set__
p = Person('tom', 18)
print(p.name)  # p.name触发__get__
print(p.age)
