# import threading
# import time
#
#
# def foo():
#     time.sleep(5)
#     for i in range(20):
#         print(i)
#
#
# # 主线程是non-daemon线程
# t = threading.Thread(target=foo, daemon=False)
# t.start()
#
# print('Main Thread Exiting')


# import threading
# import time
#
#
# def bar():
#     time.sleep(10)
#     print('bar')
#
#
# def foo():
#     for i in range(20):
#         print(i)
#     t = threading.Thread(target=bar, daemon=False)
#     t.start()
#
#
# t = threading.Thread(target=foo, daemon=True)
# t.start()
#
# time.sleep(2)
# print('Main Thread Exiting')


# import time
# import threading
#
#
# def foo(n):
#     for i in range(n):
#         print(i)
#         time.sleep(1)
#
#
# t1 = threading.Thread(target=foo, args=(20,), daemon=True)
# t1.start()
#
# t2 = threading.Thread(target=foo, args=(10,), daemon=False)
# t2.start()
#
# time.sleep(2)
# print('=========')


# import time
# import threading
#
#
# def foo(n):
#     for i in range(n):
#         print(i)
#         time.sleep(1)
#
#
# t1 = threading.Thread(target=foo, args=(10,), daemon=True)
# t1.start()
# t1.join()
#
# print('--------')


# import threading
# import time
#
#
# global_data = threading.local()
#
#
# def worker():
#     global_data.x = 0
#     for i in range(100):
#         time.sleep(0.0001)
#         global_data.x += 1
#     print(threading.current_thread(), global_data.x)
#
#
# for i in range(10):
#     threading.Thread(target=worker).start()


# import threading
# import time
# import logging
#
#
# FORMAT = '%(asctime)s %(threadName)s %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class A:
#     def __init__(self):
#         self.x = 0
#
#
# # a = A()
# a = threading.local()
#
#
# def worker():
#     a.x = 0
#     for _ in range(100):
#         time.sleep(0.001)
#         a.x += 1
#     logging.info(a.x)
#
#
# for i in range(5):
#     t = threading.Thread(target=worker, name='w-{}'.format(i))
#     t.start()
#     print(t.__dict__)


# import threading
#
#
# X = 'abc'
# ctx = threading.local()
# ctx.x = 123
#
# print(ctx, type(ctx), ctx.x)
#
#
# def worker():
#     print(X)
#     print(ctx)
#     print(ctx.x)
#     print('working')
#
#
# worker()
# print()
# threading.Thread(target=worker).start()


# import threading
# import logging
# import time
#
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(level=logging.INFO, format=FORMAT)
#
#
# def worker():
#     logging.info('in worker')
#     time.sleep(2)
#
#
# t = threading.Timer(4, worker)
# t.setName('timer')
# # t.cancel()
# t.start()
# t.cancel()
# while True:
#     print(threading.enumerate())
#     time.sleep(1)


# import threading
# import time
#
# cups = []
# flag = False
#
#
# def worker(count=10):
#     print('i am working')
#     global flag
#     while True:
#         time.sleep(0.2)
#         cups.append(1)
#         if len(cups) >= count:
#             flag = True
#             break
#     print(cups)
#
#
# def boss():
#     global flag
#     while True:
#         time.sleep(1)
#         if flag:
#             print('ok')
#             break
#
#
# b = threading.Thread(target=boss, name='boss')
# w = threading.Thread(target=worker, name='worker')
# w.start()
# b.start()


# import threading
# import time
# e = threading.Event()
#
#
# def worker(count=10):
#     cups = []
#     print('i am working')
#     while True:
#         time.sleep(0.2)
#         cups.append(1)
#         if len(cups) >= count:
#             e.set()
#             break
#     print(cups)
#
#
# def boss():
#     print('waiting')
#     e.wait()
#     print('ok')
#
#
# b = threading.Thread(target=boss, name='boss')
# w = threading.Thread(target=worker, name='worker')
# w.start()
# b.start()

# 老板雇佣了一个工人，让他生产杯子，老板一直等着这个工人，直到生产了10个杯子
# from threading import Event, Thread
# import logging
# import time
#
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# def boss(event: Event):
#     logging.info('I am boss, waiting for you.')
#     event.wait()  # 阻塞
#     logging.info('good job.')
#
#
# def worker(event: Event, count=10):
#     logging.info('I am working')
#     cups = []
#     while True:
#         logging.info('make 1')
#         time.sleep(0.5)
#         cups.append(1)
#         if len(cups) >= count:
#             event.set()
#             break
#     logging.info('I finished my job. cups={}'.format(cups))
#
#
# event = Event()
# w = Thread(target=worker, args=(event,))
# b = Thread(target=boss, args=(event,))
# w.start()
# b.start()





















































































