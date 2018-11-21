#
# XClass = type('myclass', (object,), {'a': 100, 'b': 'string'})
# print(XClass)
# print(XClass.__dict__)
# print(XClass.__name__)
# print(XClass.__bases__)
# print(XClass.mro())


# def __init__(self):
#     self.x = 1000
#
#
# def show(self):
#     print(self.x)
#
#
# XClass = type('myclass', (object,), {
#     'a': 100, 'b': 'string', 'show': show, '__init__': __init__
# })  # 字典是类属性
#
# print(XClass)
# print(XClass.__dict__)
# print(XClass.__name__)
# print(XClass.__bases__)
# print(type(XClass))
# print(XClass.mro())
# XClass().show()

# class ModelMeta(type):  # 继承自type
#     def __new__(cls, name, bases, attrs: dict):
#         print(cls)
#         print(name)
#         print(bases)
#         print(attrs)
#         return super().__new__(cls, name, bases, attrs)
#
#
# class A(metaclass=ModelMeta):  # 使用metaclass关键字参数指定元类
#     id = 100
#
#     def __init__(self):
#         print('A.ini')
#
#
# class B(A):  # B继承自A后，依然是ModelMeta的类型
#     pass
#
#
# C = ModelMeta('Cclass', (), {'t': 9})  # 使用元类创建新的类


# 元类应用
# class Field:
#     def __init__(self, fieldname=None, pk=False, nullable=True):
#         self.fieldname = fieldname
#         self.pk = pk
#         self.nullable = nullable
#
#     def __repr__(self):
#         return "Field {}".format(self.fieldname)
#
#
# class ModelMeta(type):
#     def __new__(cls, name, bases, attrs: dict):
#         print(cls)
#         print(name)
#         print(bases)
#         print(attrs, '--------------')
#
#         if '__tablename__' not in attrs.keys():
#             attrs['__tablename__'] = name
#
#         primarykeys = []
#         for k, v in attrs.items():  # k,v是 id:Field()
#             if isinstance(v, Field):
#                 if v.fieldname is None:
#                     v.fieldname = k  # 没有名字则使用属性名
#                 if v.pk:
#                     primarykeys.append(v)
#
#         attrs['__primarykeys__'] = primarykeys
#         return super().__new__(cls, name, bases, attrs)
#
#
# class ModelBase(metaclass=ModelMeta):
#     pass
#
#
# class Student(ModelBase):
#     id = Field(pk=True, nullable=False)
#     name = Field('username', nullable=False)
#     age = Field()
#
#
# print('---------------------')
# print(Student.__dict__)













