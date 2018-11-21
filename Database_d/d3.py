# import sqlalchemy
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# USER = 'zoes'
# PWD = 'zoes'
# HOST = '172.16.203.24'
# PORT = 3306
# DB = 'test'
#
#
# engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(
#     USER, PWD, HOST, PORT, DB
# ), echo=True)
#
# Base = declarative_base()
#
#
# class Student(Base):
#     __tablename__ = 'student'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64), nullable=False)
#     age = Column(Integer)
#
#     def __repr__(self):
#         return "{} id={} name={} age={}".format(
#             self.__class__.__name__, self.id, self.name, self.age
#         )
#
#
# # s = Student(name='tom')
# # print(s.name)
# # s.age = 20
# # print(s.age)
#
# # Base.metadata.create_all(engine)
#
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # session.add(s)
# # print(s)
# # session.commit()
# # print(s)
# # print('================')
#
# # s = Student(name='joe', age=24)
# # session.add(s)
# # session.commit()
#
#
# # student = session.query(Student).get(1)
# # print(student)
#
# # student = session.query(Student)
# # print(1, list(student))
#
# student = session.query(Student).get(2)
# print(student)
# student.name = 'sam'
# student.age = 30
# print(student)
# session.add(student)
# session.commit()


# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# user = 'zoes'
# pwd = 'zoes'
# host = '172.16.203.24'
# port = 3306
# db = 'test'
#
# engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(
#     user, pwd, host, port, db
# ), echo=True)
#
# Base = declarative_base()  # 基类
#
#
# # Mapper 创建实体类
# class Student(Base):
#     # 指定表名
#     __tablename__ = 'student'
#     # 定义类属性对应字段
#     # 定义类属性字段名，如果和属性名一致，一定要指定
#     # age = Column('age', Integer)
#     id = Column(Integer, primary_key=True)  # 字段定义，类属性
#     name = Column(String(64), nullable=False)
#     age = Column(Integer)
#
#     def __repr__(self):
#         return '<{} {} {} {}>'.format(
#             self.__class__.__name__, self.id, self.name, self.age
#         )


# s = Student(name='tommy')
# print(repr(Student.__table__))
# print(s)
# s.age = 30
# print(s)
# # 删除继承自Base的所有表
# Base.metadata.drop_all(bind=engine)
# # 创建继承自Base的所有表
# Base.metadata.create_all(bind=engine)

# 创建session
# Session = sessionmaker(bind=engine)  # 返回类
# session = Session()  # 实例化，第一次使用时连接数据库

# session.add(s)
# print(1, s)
# session.commit()
# print(2, s)
# print('~~~~~~~~~~~~~~~')
#
# try:
#     session.add_all([s])
#     print(3, s)
#     session.commit()
#     print(4, s)
# except:
#     session.rollback()
#     raise


# students = session.query(Student)  # 无条件
# for i in students:
#     print(i)
# print('-'*30)
#
# student = session.query(Student).get(2)  # 通过主键查询
# print(student)


# try:
#     student = Student(id=2, name='sam', age=30)
#     session.delete(student)
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()
#     print('---------------')


# import sqlalchemy
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# user = 'zoes'
# pwd = 'zoes'
# host = '172.16.203.24'
# port = 3306
# db = 'test'
#
# engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(
#     user, pwd, host, port, db
# ), echo=True)
#
# Base = declarative_base()
#
#
# class Student(Base):
#     __tablename__ = 'student'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(64), nullable=False)
#     age = Column(Integer)
#
#     def __repr__(self):
#         return '{} id={} name={} age={}'.format(
#             self.__class__.__name__, self.id, self.name, self.age
#         )
#
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# from sqlalchemy.orm.state import InstanceState
#
#
# def getstate(entity, i):
#     insp = sqlalchemy.inspect(entity)
#     state = "session_id={}, attached={}\ntransient={}, " \
#             "persistent={}\npending={}, deleted={}, " \
#             "detached={}".format(
#         insp.session_id,
#         insp._attached,
#         insp.transient,
#         insp.persistent,
#         insp.pending,
#         insp.deleted,
#         insp.detached
#     )
#     print(i, state)
#     print(insp.key)
#     print('=' * 30)
#
#
# student = session.query(Student).get(3)
# getstate(student, 1)  # persistent
#
# try:
#     student = Student(id=2, name='sam', age=30)
#     getstate(student, 2)  # transient
#     student = Student(name='sammy', age=30)
#     getstate(student, 3)  # transient
#     session.add(student)
#     getstate(student, 4)  # pending
#     # session.delete(student)  # 删除的前提是persistent，否则抛异常
#     # getstate(student, 5)
#     session.commit()
#     getstate(student, 6)  # persistent
# except Exception as e:
#     session.rollback()
#     print('~~~~~~~~~~~~~~~~~')
#     print(e)
#
# student = session.query(Student).get(3)
# getstate(student, 10)  # persistent
#
# try:
#     session.delete(student)  # 删除的前提是persistent，否则抛异常
#     getstate(student, 11)  # persistent
#     session.flush()
#     getstate(student, 12)  # deleted
#     session.commit()
#     getstate(student, 13)  # detached
# except Exception as e:
#     session.rollback()
#     print('~~~~~~~~~~~~~~~~~')
#     print(e)

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, \
Enum, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
import enum

user = 'zoes'
pwd = 'zoes'
host = '172.16.203.24'
port = 3306
db = 'test'

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
    user, pwd, host, port, db
), echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class MyEnum(enum.Enum):  # python中的枚举
    M = 'M'
    F = 'F'


class Employee(Base):
    # 指定表名
    __tablename__ = 'employees'

    # 定义属性对应字段
    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(MyEnum), nullable=False)
    hire_date = Column(Date, nullable=False)

    def __repr__(self):
        return "{} no={} name={} {} gender={}".format(
            self.__class__.__name__, self.emp_no,
            self.first_name, self.last_name, self.gender.value
        )


# 打印函数
def show(emps):
    for i in emps:
        print(i)
    print('-'*30, end='\n\n')


# 简单条件查询
# emps = session.query(Employee).filter(Employee.emp_no > 10015)
# show(emps)

# 与或非
from sqlalchemy import or_, and_, not_

# AND条件
# emps = session.query(Employee).filter(Employee.emp_no > 10015)\
#     .filter(Employee.gender == MyEnum.F)
# show(emps)

# emps = session.query(Employee).filter(
#     and_(Employee.emp_no > 10015, Employee.gender == MyEnum.F)
# )
# show(emps)

# emps = session.query(Employee).filter(
#     (Employee.emp_no > 10015) & (Employee.gender == MyEnum.F)
# )  # 一定要注意& 符号两边表达式都要加括号
# show(emps)

# OR条件
# emps = session.query(Employee).filter(
#     (Employee.emp_no > 10018) | (Employee.emp_no < 10003)
# )
# show(emps)

# emps = session.query(Employee).filter(
#     or_(Employee.emp_no > 10018, Employee.emp_no < 10003)
# )
# show(emps)

# NOT
# emps = session.query(Employee).filter(
#     not_(Employee.emp_no < 10018)
# )
# show(emps)

# emps = session.query(Employee).filter(
#     ~(Employee.emp_no < 10018) & (Employee.gender == MyEnum.F)
# )  # 一定要加括号
# show(emps)
# # 总之，与或非的运算符&、|、~、一定要在表达式加上括号

# in
# emplist = [10010, 10015, 10018]
# emps = session.query(Employee).filter(
#     Employee.emp_no.in_(emplist)
# )
# show(emps)

# not in
# emps = session.query(Employee).filter(
#     ~Employee.emp_no.in_(emplist)
# )
# show(emps)

# emps = session.query(Employee).filter(
#     Employee.emp_no.notin_(emplist)
# )
# show(emps)

# like
# emps = session.query(Employee).filter(
#     Employee.last_name.like('p%')
# )
# show(emps)

# not like
# emps = session.query(Employee).filter(
#     Employee.last_name.notlike('P%')
# )
# show(emps)
# ilike可以忽略大小写匹配


# 排序
# 升序
# emps = session.query(Employee).filter(
#     Employee.emp_no > 10010
# ).order_by(Employee.emp_no)
# show(emps)

# 降序
# emps = session.query(Employee).filter(
#     Employee.emp_no > 10010
# ).order_by(Employee.emp_no.desc())
# show(emps)

# 多列排序
# emps = session.query(Employee).filter(
#     Employee.emp_no > 10010
# ).order_by(Employee.last_name).order_by(Employee.emp_no.desc())
# show(emps)

# 分页
# emps = session.query(Employee).limit(4)
# show(emps)
#
# emps = session.query(Employee).limit(4).offset(15)
# show(emps)

# 消费者方法
# 总行数
# emps = session.query(Employee)
# print(1, len(list(emps)))  # 返回大量的结果集，然后转换list
# print(2, emps.count())  # 聚合函数count(*)的查询,SQL语句中有子查询

# 取所有数据
# emps = session.query(Employee)
# print(emps.all())  # 返回列表，查不到返回空列表
# # 取首行
# print(emps.first())  # 返回首行，查不到返回None
# # 有且只能有一行
# # print(emps.one())  # 如果查询结果是多行则抛异常
# print(emps.limit(1).one())
#
# # 删除 deleted by query
# session.query(Employee).filter(Employee.emp_no > 10018).delete()
# # session.commit()  # 提交则删除


# 聚合函数
from sqlalchemy import func
# query = session.query(func.count(Employee.emp_no))
# print(query.one())  # 只能有一行结果，返回元组
# print(query.scalar())  # 取one()返回元组的第一个元素

# max/min/avg
# print(session.query(func.max(Employee.emp_no)).scalar())
# print(session.query(func.min(Employee.emp_no)).scalar())
# print(session.query(func.avg(Employee.emp_no)).scalar())

# 分组
# print(session.query(
#     Employee.gender, func.count(Employee.emp_no)
# ).group_by(Employee.gender).all())











































































