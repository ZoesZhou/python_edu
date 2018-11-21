# import pymysql
# conn = None
# cursor = None
# try:
#     conn = pymysql.connect('172.16.203.24', 'zoes', 'zoes', 'test')
#     print(conn)
#
#     insert_sql = "insert into user (name, loginname, password) " \
#                  "values('sam3', 'sam3', 'sam3')"
#     cursor = conn.cursor()
#
#     cursor.execute(insert_sql)
#     conn.commit()
# except Exception as e:
#     conn.rollback()
#     print(e)
# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()


# import pymysql
# conn = None
# cursor = None
# try:
#     conn = pymysql.connect('172.16.203.24', 'zoes', 'zoes', 'test')
#     print(conn)
#
#     sql = "select * from user"
#     cursor = conn.cursor(pymysql.cursors.DictCursor)
#     count = cursor.execute(sql)
#     print(count)
#
#     rows = cursor.fetchall()
#     print(rows)
#     conn.commit()
#
# except Exception as e:
#     conn.rollback()
#     print(e)
# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()


# import pymysql
#
#
# conn = pymysql.connect('172.16.203.24', 'zoes', 'zoes', 'test')
# cursor = conn.cursor()
# try:
#     for i in range(10, 15):
#         insert_sql = "insert into user (name, loginname, password) " \
#                      "values('sam', 'sam{}', 'sam3')".format(i)
#         cursor.execute(insert_sql)
#     conn.commit()
# except Exception as e:
#     conn.rollback()
#     print(e)
# finally:
#     cursor.close()
#     conn.close()


# # 注入攻击
# import pymysql
# conn = None
# cursor = None
# try:
#     conn = pymysql.connect('172.16.203.24', 'zoes', 'zoes', 'test')
#     print(conn)
#     user = "zhou"
#     pwd = "1100' or '1'='1"
#     sql = "select * from user where loginname = '{}' and " \
#           "password = '{}'".format(user, pwd)
#     cursor = conn.cursor(pymysql.cursors.DictCursor)
#     count = cursor.execute(sql)
#     print(sql)
#     print(count)
#     rows = cursor.fetchall()
#     print(rows)
#     conn.commit()
# except Exception as e:
#     print(e)
#     conn.rollback()
# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()


# # 参数化查询
# import pymysql
# conn = None
# cursor = None
# try:
#     conn = pymysql.connect('172.16.203.24', 'zoes', 'zoes', 'test')
#     print(conn)
#     user = "zhou"
#     pwd = "1100' or '1'='1"
#     sql = "select * from user where id = %s"
#     cursor = conn.cursor()  # 结果集
#     count = cursor.execute(sql, ["1 or 2 = 2"])
#     print(sql)
#     print(count)
#     rows = cursor.fetchall()
#     print(rows)
#     conn.commit()
# except Exception as e:
#     conn.rollback()
#     print(e)
# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()


# # 参数化查询
# import pymysql
#
#
# conn = pymysql.connect('172.16.203.24', 'zoes', 'zoes', 'test')
# cursor = conn.cursor()
# userid = '3 or 2=2'
# sql = 'select * from user where id = %s'
# cursor.execute(sql, [userid])
# rows = cursor.fetchall()
# print(rows)
# print('-'*30)
# sql = 'select * from user where loginname = %(loginname)s ' \
#       'and password = %(password)s'
# cursor.execute(sql, {'loginname': 'zhou', 'password': '1100'})
# print(cursor.fetchall())
#
# if cursor:
#     cursor.close()
# if conn:
#     conn.close()

# 支持上下文
# import pymysql
#
#
# conn = pymysql.connect('172.16.203.24', 'zoes', 'zoes', 'test')
# print(conn)
# with conn as cursor:
#     sql = "select * from user"
#     cursor.execute(sql)
#     print(cursor.fetchall())
#     # sql = "insert into user (name, loginname, password) " \
#     #     "values(%s, %s, %s)"
#     # print(sql)
#     # rows = cursor.executemany(sql, [('joe{}'.format(i),
#     #                                 'joe{}'.format(i),
#     #                                  'joe{}'.format(i))
#     #                                 for i in range(30, 35)])
#     cursor.close()
#     # 如果此时使用这个关闭的cursor，就会抛异常
#     # sql = "select * from user"
#     # cursor.execute(sql)
#     # print(cursor.fetchall())
# conn.close()


# import pymysql
#
#
# conn = pymysql.connect('172.16.203.24', 'zoes', 'zoes', 'test')
# try:
#     with conn.cursor() as cursor:
#         sql = "select * from user"
#         print(cursor.execute(sql))
#         print(cursor.fetchall())
#     conn.commit()
#     # 如果此时使用这个关闭的cursor，会抛异常
#     # sql = "select * from user"
#     # print(cursor.execute(sql))
#     # print(cursor.fetchall())
# except Exception as e:
#     print(e)
#     conn.rollback()
# finally:
#     conn.close()


import pymysql


conn = pymysql.connect('172.16.203.24', 'zoes', 'zoes', 'test')

with conn as cursor:
    with cursor:
        sql = "select * from user"
        print(cursor.execute(sql))
        print(cursor.fetchall())


conn.close()














































































