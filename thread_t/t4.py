# from threading import Event, Thread
# import logging
# import time
# logging.basicConfig(level=logging.INFO)
#
#
# def do(event: Event, interval: int):
#     while not event.wait(interval):  # 等待超时返回False
#         logging.info('do sth')
#
#
# event = Event()
# Thread(target=do, args=(event, 3)).start()
#
# event.wait(10)  # 主线程阻塞10s
# # time.sleep(10)
# event.set()
# print('main exit')
# from threading import Event, Thread
#
#
# class Timer:
#     def __init__(self, interval, function, args=(), kwargs={}):
#         self.interval = interval
#         self.function = function
#         self.args = args
#         self.kwargs = kwargs
#         self.event = Event()
#
#     def start(self):
#         self.event.wait(self.interval)
#         if not self.event.is_set():
#             # self.function(*self.args, **self.kwargs)
#             th = Thread(target=self.function, args=self.args, kwargs=self.kwargs)
#             th.start()
#         self.event.set()
#
#     def cancel(self):
#         self.event.set()
#
#
# def add(x, y):
#     print(x + y)
#
#
# t = Timer(1, add, (4, 5))
# t.start()  # 堵塞
# t.cancel()
# print('====')

# from threading import Event, Thread
#
#
# class Timer:
#     def __init__(self, interval, function, args=None, kwargs=None):
#         self.interval = interval
#         self.function = function
#         self.args = args if args is not None else []
#         self.kwargs = kwargs if kwargs is not None else {}
#         self.event = Event()
#
#     def start(self):
#         t = Thread(target=self.run)
#         t.start()
#
#     def run(self):
#         self.event.wait(self.interval)
#         if not self.event.wait(self.interval):
#             self.function(*self.args, **self.kwargs)
#         self.event.set()
#
#     def cancel(self):
#         self.event.set()
#
#
# def add(x=4, y=5):
#     print(x + y)
#
#
# t1 = Timer(1, add, (6, 7))
# print(t1.__dict__, '---')
# # t1.cancel()
# t1.start()
# print('=====')


# 订单需求生产1000个杯子，组织10个工人生产
# import threading
# import logging
# import time
# from threading import Thread, Lock
#
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# cups = []
# lock = Lock()
#
#
# def worker(count=10):
#     logging.info('I am working.')
#     lock.acquire()
#     while len(cups) < count:
#         time.sleep(0.0001)
#         cups.append(1)
#     lock.release()
#     logging.info('I finished. cups = {}'.format(len(cups)))
#
#
# for _ in range(10):
#     Thread(target=worker, args=(1000,)).start()


# import threading
# import logging
# import time
# from threading import Thread, Lock
#
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# cups = []
# lock = Lock()
#
#
# def worker(count=10):
#     logging.info("I'm working")
#     flag = False
#     while True:
#         lock.acquire()
#
#         if len(cups) >= count:  # 999
#             flag = True
#
#         # lock.release()
#
#         time.sleep(0.001)
#         if not flag:
#             cups.append(1)
#
#         lock.release()
#
#         if flag:
#             break
#         # lock.release()
#     logging.info('I finish. cups = {}'.format(len(cups)))
#
#
# for _ in range(10):
#     Thread(target=worker, args=(1000,)).start()


# import threading
# import time
# from threading import Thread, Lock
#
#
# class Counter:
#     def __init__(self):
#         self._val = 0
#         self.lock = Lock()
#
#     @property
#     def value(self):
#         with self.lock:
#           return self._val
#
#     def inc(self):
#         with self.lock:
#             self._val += 1
#
#     def dec(self):
#         try:
#             self.lock.acquire()
#             self._val -= 1
#         finally:
#             self.lock.release()
#
#
# def run(c: Counter, count=100):
#     for _ in range(count):
#         for i in range(-50, 50):
#             if i < 0:
#                 c.dec()
#             else:
#                 c.inc()
#
#
# c = Counter()
# c1 = 10  # 线程数
# c2 = 1000
# for i in range(c1):
#     Thread(target=run, args=(c, c2)).start()
#
# # print(c.value)
# while True:
#     time.sleep(1)
#     if threading.active_count() == 1:  # 工作线程结束，只剩主线程
#         print(threading.enumerate())
#         print(c.value)
#         break
#     # else:
#     #     print(threading.enumerate())


# import threading
# import logging
# import time
#
#
# FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# def worker(tasks):
#     for task in tasks:
#         time.sleep(0.001)
#         if task.lock.acquire(False):  # 非阻塞，获取锁则返回True
#             logging.info('{} {} begin to start'.format(threading.current_thread(), task.name))
#         else:
#             logging.info('{} {} is working'.format(threading.current_thread(), task.name))
#
#
# class Task:
#     def __init__(self, name):
#         self.name = name
#         self.lock = threading.Lock()
#
#
# # 构造10个任务
# tasks = [Task('task-{}'.format(x)) for x in range(10)]
#
#
# for i in range(5):
#     threading.Thread(target=worker, name='worker-{}'.format(i), args=(tasks,)).start()


# import threading
# import time
#
#
# lock = threading.RLock()
# print(lock.acquire())
# print('-----------------')
# print(lock.acquire(blocking=False))
# print(lock.acquire())
# print(lock.acquire(timeout=3.55))
# # print(lock.acquire(blocking=False, timeout=10))
# lock.release()
# lock.release()
# lock.release()
# lock.release()
# print('main thread {}'.format(threading.current_thread().ident))
# print("lock in main thread {}".format(lock))
# # lock.release()
# print('=================')
# print()
#
# print(lock.acquire(blocking=False))
# # threading.Timer(3, lambda x: x.release(), args=(lock,)).start()
# lock.release()
# print('~~~~~~~~~~~~~~~')
# print()
#
# print(lock.acquire())
#
#
# def sub(l):
#     print('{}: {}'.format(threading.current_thread(), l.acquire()))
#     print('{}: {}'.format(threading.current_thread(), l.acquire(False)))
#     print('lock in sub thread {}'.format(lock))
#     l.release()
#     print('sub 1')
#     l.release()
#     print('sub 2')
#     # l.release()
#
#
# threading.Timer(2, sub, args=(lock,)).start()
# print('+++++++++++++++++++')
# print()
#
# print(lock.acquire())
# lock.release()
# print('释放主线程锁')
# lock.release()


# from threading import RLock, Thread
# import logging
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# lock = RLock()
# # print(1, lock)
# # lock.acquire()
# # lock.acquire(False)
# # print(2, lock)
# # lock.release()
# # print(3, lock)
#
#
# def sub(l):
#     logging.info('------in sub thread')
#     l.acquire()
#     logging.info('~~~~~~end sub')
#     print(5, lock)
#
#
# # sub(lock)
# t = Thread(target=sub, args=(lock,)).start()
#
#
# print(4, lock)


from threading import Thread, Event, Condition
import logging
import random


FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class Dispatcher:
    def __init__(self):
        self.data = None
        self.event = Event()
        self.cond = Condition()

    def produce(self, total):
        for _ in range(total):
            data = random.randint(0, 100)
            with self.cond:
                logging.info(data)
                self.data = data
                self.cond.notify(n=2)
            self.event.wait(1)
        self.event.set()

    def consume(self):  # 速度不匹配，消费者主动查看有没有数据
        while not self.event.is_set():
            with self.cond:
                self.cond.wait()
                logging.info('received {}'.format(self.data))
                self.data = None
            self.event.wait(0.5)


d = Dispatcher()
p = Thread(target=d.produce, args=(10,), name='produce')

for _ in range(2):
    Thread(target=d.consume, name='consumer').start()

p.start()
print('---------')

































































































