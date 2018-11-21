# import sqlalchemy
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Date, \
#     ForeignKey, create_engine, Enum
# from sqlalchemy.orm import sessionmaker, relationship
# import enum
#
# user = 'zoes'
# pwd = 'zoes'
# host = '172.16.203.24'
# port = 3306
# db = 'test'
#
# engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
#     user, pwd, host, port, db
# ), echo=True)
# Base = declarative_base()
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# class MyEnum(enum.Enum):
#     M = 'M'
#     F = 'F'
#
#
# class Employee(Base):
#     __tablename__ = 'employees'
#     emp_no = Column(Integer, primary_key=True)
#     birth_date = Column(Date, nullable=False)
#     first_name = Column(String(14), nullable=False)
#     last_name = Column(String(16), nullable=False)
#     gender = Column(Enum(MyEnum), nullable=False)
#     hire_date = Column(Date, nullable=False)
#
#     departments = relationship('Dept_emp')
#
#     def __repr__(self):
#         return "{} no={} name={} {} gender={}, depts={}".format(
#             self.__class__.__name__, self.emp_no,
#             self.first_name, self.last_name, self.gender,
#             self.departments
#         )
#
#
# class Department(Base):
#     __tablename__ = 'departments'
#     dept_no = Column(String(4), primary_key=True)
#     dept_name = Column(String(40), nullable=False, unique=True)
#
#     def __repr__(self):
#         return "{} no={} name={}".format(
#             type(self).__name__, self.dept_no, self.dept_name
#         )
#
#
# class Dept_emp(Base):
#     __tablename__ = 'dept_emp'
#     emp_no = Column(Integer, ForeignKey(
#         'employees.emp_no', ondelete='CASCADE'
#     ), primary_key=True)
#     dept_no = Column(String(4), ForeignKey(
#         'departments.dept_no', ondelete='CASCADE'
#     ), primary_key=True)
#     from_date = Column(Date, nullable=False)
#     to_date = Column(Date, nullable=False)
#
#     def __repr__(self):
#         return "{} emp_no={} dept_no={}".format(
#             type(self).__name__, self.emp_no, self.dept_no
#         )
#
#
# def show(results):
#     for i in results:
#         print(i)
#     print('-'*30, end='\n\n')


# results = session.query(Dept_emp).filter(Dept_emp.emp_no == 10009).all()
# show(results)

# results = session.query(Employee, Dept_emp).filter(
#     Employee.emp_no == 10009
# ).all()
# show(results)


# 查询10010员工的所在的部门编号及员工信息(使用第三张关系表)
# sql = "select employees.*, dept_emp.* from employees, dept_emp
#         where employees.emp_no = dept_emp.emp_no
#          and employees.emp_no == 10010"
# results = session.query(Employee, Dept_emp).filter(
#     Employee.emp_no == Dept_emp.emp_no
# ).filter(Employee.emp_no == 10010).all()
# show(results)

# 使用join查询10010员工的所在的部门编号及员工信息
# 第一种写法
# results = session.query(Employee).join(
#     Dept_emp, Employee.emp_no == Dept_emp.emp_no
# ).filter(Employee.emp_no == 10010).all()
# print(results)


import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Date, \
ForeignKey, Enum, create_engine
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


class MyEnum(enum.Enum):
    M = 'M'
    F = 'F'


class Employee(Base):
    __tablename__ = 'employees'
    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(MyEnum), nullable=False)
    hire_date = Column(Date, nullable=False)

    departments = relationship('Dept_emp')
    titles = relationship('Title')

    def __repr__(self):
        return "{} no={} name={} {} gender={} depts={} titles={}".format(
            type(self).__name__,
            self.emp_no,
            self.first_name,
            self.last_name,
            self.gender,
            self.departments,
            self.titles
        )


class Department(Base):
    __tablename__ = 'departments'
    dept_no = Column(String(4), primary_key=True)
    dept_name = Column(String(40), nullable=False, unique=True)

    def __repr__(self):
        return "{} dept_no={} dept_name={}".format(
            type(self).__name__, self.dept_no, self.dept_name
        )


class Dept_emp(Base):
    __tablename__ = 'dept_emp'
    emp_no = Column(Integer, ForeignKey(
        'employees.emp_no', ondelete='CASCADE'
    ), primary_key=True)
    dept_no = Column(String(4), ForeignKey(
        'departments.dept_no', ondelete='CASCADE'
    ), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    departments = relationship('Department')

    def __repr__(self):
        return "{} emp_no={} dept_no={} dept_name={}".format(
            type(self).__name__, self.emp_no, self.dept_no,
            self.departments
        )


class Title(Base):
    __tablename__ = 'titles'
    emp_no = Column(Integer, ForeignKey(
        'employees.emp_no', ondelete='CASCADE'
    ), primary_key=True)
    title = Column(String(50), primary_key=True)
    from_date = Column(Date, primary_key=True)
    to_date = Column(Date, nullable=False)

    def __repr__(self):
        return "{} emp_no={} title {}".format(
            type(self).__name__, self.emp_no, self.title
        )


# 10009号员工的工号，姓名，所有的 头衔
# results = session.query(Employee).join(
#     Dept_emp, Employee.emp_no == Dept_emp.emp_no
# ).filter(Employee.emp_no == 10009).all()
# print(results)

# 10010号员工的姓名及所在部门名称
# results = session.query(Employee).join(
#     Dept_emp, Employee.emp_no == Dept_emp.emp_no
# ).filter(Employee.emp_no == 10010).all()
# print(results)

# sql语句
# sql = "select ee.first_name, ee.last_name, dept_emp.dept_no, departments.dept_name from employees as ee
# join dept_emp on ee.emp_no = dept_emp.emp_no join departments on dept_emp.dept_no = departments.dept_no
# where ee.emp_no = 10010"

results = session.query(Employee).join(
    Dept_emp, Employee.emp_no == Dept_emp.emp_no
).join(Department, Dept_emp.dept_no == Department.dept_no).filter(
    Employee.emp_no == 10010
).all()
print(results)










































































