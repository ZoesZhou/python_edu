# 对实例的数据进行校验
# class Person:
#     def __init__(self, name: str, age: int):
#         params = ((name, str), (age, int))
#         if not self.check_data(params):
#             raise TypeError
#         print('ok=======')
#         self.name = name
#         self.age = age
#
#     def check_data(self, params):
#         for p, t in params:
#             if not isinstance(p, t):
#                 return False
#             # else:
#         print('-----')
#         return True
#
#
# p = Person('tom', 20)


# 硬编码
# class TypeCheck:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#         self.data = {}
#
#     def __get__(self, instance, owner):
#         print('get')
#         if instance is not None:
#             return instance.__dict__[self.name]
#             # return self.data[self.name]
#             # return getattr(self, self.name)  # 报错
#         return self  # return和break作用等同
#
#     def __set__(self, instance, value):  # instance=Person的实例
#         print('set')
#         if not isinstance(value, self.kind):
#             raise TypeError
#         instance.__dict__[self.name] = value
#         # self.data[self.name] = value
#         # setattr(self, self.name, value)  # 报错
#         # 产生递归，相当于self.name=value,又会触发__get__
#         # setattr(instance, self.name, value)  # 不能这么写
#
#
# class Person:
#     name = TypeCheck('name', str)  # 构成描述器
#     age = TypeCheck('age', int)
#
#     def __init__(self, name: str, age: int):
#         self.name = name  # 触发__set__
#         self.age = age
#
#
# # Person实例化的时候,self.name,self.age触发__set__
# p = Person('tom', 18)
# print(p.name)  # p.name触发__get__
# print(p.age)


# 用函数装饰器从__init__()获取参数类型，来把实例属性变成描述器
# class TypeCheck:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#         self.data = {}
#
#     def __get__(self, instance, owner):
#         print('get')
#         if instance is not None:
#             return instance.__dict__[self.name]
#             # return self.data[self.name]
#             # return getattr(self, self.name)  # 报错
#         return self  # return和break作用等同
#
#     def __set__(self, instance, value):  # instance=Person的实例
#         print('set')
#         if not isinstance(value, self.kind):
#             raise TypeError
#         instance.__dict__[self.name] = value
#         # self.data[self.name] = value
#         # setattr(self, self.name, value)  # 报错
#         # 产生递归，相当于self.name=value,又会触发__get__
#         # setattr(instance, self.name, value)  # 不能这么写
#
#
# import inspect
#
#
# def type_assert(cls):
#     sig = inspect.signature(cls)
#     params = sig.parameters  # params是有序字典
#     for name, param in params.items():
#         if param.annotation != param.empty:
#             setattr(cls, name, TypeCheck(name, param.annotation))
#     return cls
#
#
# @type_assert
# class Person:
#     # name = TypeCheck('name', str)  # 构成描述器
#     # age = TypeCheck('age', int)
#
#     def __init__(self, name: str, age: int):
#         self.name = name  # 触发__set__
#         self.age = age
#
#
# # Person实例化的时候,self.name,self.age触发__set__
# p = Person('tom', 18)
# print(p.name)  # p.name触发__get__
# print(p.age)


# 用类装饰器从__init__()获取参数类型，来把实例属性变成描述器
# class TypeCheck:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#         self.data = {}
#
#     def __get__(self, instance, owner):
#         print('get')
#         if instance is not None:
#             return instance.__dict__[self.name]
#             # return self.data[self.name]
#             # return getattr(self, self.name)  # 报错
#         return self  # return和break作用等同
#
#     def __set__(self, instance, value):  # instance=Person的实例
#         print('set')
#         if not isinstance(value, self.kind):
#             raise TypeError
#         instance.__dict__[self.name] = value
#         # self.data[self.name] = value
#         # setattr(self, self.name, value)  # 报错
#         # 产生递归，相当于self.name=value,又会触发__get__
#         # setattr(instance, self.name, value)  # 不能这么写
#
#
# import inspect
#
#
# class TypeAssert:
#     def __init__(self, cls):
#         self.cls = cls
#         sig = inspect.signature(cls)
#         params = sig.parameters  # params是有序字典
#         for name, param in params.items():
#             if param.annotation != param.empty:
#                 setattr(cls, name, TypeCheck(name, param.annotation))
#
#     def __call__(self, name, age):
#         return self.cls(name, age)
#
#
# @TypeAssert  # Person=TypeAssert(Person)
# class Person:
#     # name = TypeCheck('name', str)  # 构成描述器
#     # age = TypeCheck('age', int)
#
#     def __init__(self, name: str, age: int):
#         self.name = name  # 触发__set__
#         self.age = age
#
#
# # Person实例化的时候,self.name,self.age触发__set__
# p = Person('tom', 18)
# print(p.name)  # p.name触发__get__
# print(p.age)























