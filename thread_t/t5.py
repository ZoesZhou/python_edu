# from threading import Thread, Event, Condition
# import logging
# import random
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class Dispatcher:
#     def __init__(self):
#         self.data = None
#         self.event = Event()
#         self.cond = Condition()
#
#     def produce(self, total):
#         for _ in range(total):
#             data = random.randint(0, 100)
#             with self.cond:
#                 logging.info(data)
#                 self.data = data
#                 self.cond.notify_all()
#             self.event.wait(1)
#         self.event.set()
#
#     def consume(self):  # 速度不匹配，消费者主动查看有没有数据
#         while not self.event.is_set():
#             with self.cond:
#                 self.cond.wait()
#                 logging.info('received {}'.format(self.data))
#                 self.data = None
#             self.event.wait(0.5)
#
#
# d = Dispatcher()
# p = Thread(target=d.produce, args=(10,), name='produce')
# c = Thread(target=d.consume, name='consumer')
# c.start()
# p.start()
# print('p----')


# from threading import Barrier
# import logging
# import threading
#
#
# FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# def worker(barrier: Barrier):
#     logging.info('waiting for {} threads.'.format(barrier.n_waiting))
#     try:
#         barrier_id = barrier.wait()
#         logging.info('after barrier {}'.format(barrier_id))
#     except threading.BrokenBarrierError:
#         logging.info('Broken Barrier')
#
#
# barrier = Barrier(3)
# for x in range(3):
#     threading.Thread(target=worker, name='worker={}'.format(x), args=(barrier,)).start()
#
# logging.info('started')


# import threading
# import logging
#
#
# FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# def worker(barrier: threading.Barrier):
#     logging.info('waiting for {} threads.'.format(barrier.n_waiting))
#     try:
#         barrier_id = barrier.wait()
#         logging.info('after barrier {}'.format(barrier_id))
#     except threading.BrokenBarrierError:
#         logging.info('Broken Barrier .run.')
#
#
# barrier = threading.Barrier(3)
# for x in range(9):
#     if x == 2:
#         barrier.abort()
#     elif x == 6:
#         barrier.reset()
#     threading.Event().wait(1)
#     threading.Thread(target=worker, name='worker-{}'.format(x), args=(barrier,)).start()


# import threading
# import logging
#
#
# FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# def worker(barrier: threading.Barrier, i: int=2):
#     logging.info('waiting for {} thread.'.format(barrier.n_waiting))
#     try:
#         logging.info(barrier.broken)
#         if i < 3:
#             barrier_id = barrier.wait(1)
#         else:
#             if i == 6:
#                 barrier.reset()
#             barrier_id = barrier.wait()
#         logging.info('after barrier {}'.format(barrier_id))
#     except threading.BrokenBarrierError:
#         logging.info('Broken Barrier . run.')
#
#
# barrier = threading.Barrier(3)
# for x in range(9):
#     threading.Event().wait(2)
#     threading.Thread(target=worker, name='worker-{}'.format(x), args=(barrier,)).start()


# import threading
# import logging
# import time
#
#
# FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# def worker(s: threading.Semaphore):
#     logging.info('in sub thread')
#     logging.info(s.acquire())  # 阻塞
#     logging.info('sub thread over')
#
#
# s = threading.Semaphore(3)
# logging.info(s.acquire())
# print(s._value)
# logging.info(s.acquire())
# print(s._value)
# logging.info(s.acquire())
# print(s._value)
# threading.Thread(target=worker, args=(s,)).start()
# time.sleep(2)
# logging.info(s.acquire(False))  # 不阻塞，返回False
# logging.info(s.acquire(timeout=3))  # 阻塞3秒，返回False
#
# logging.info('release')
# s.release()


# import logging
# import threading
#
#
# sema = threading.Semaphore(3)
# logging.warning(sema.__dict__)
# for i in range(3):
#     sema.acquire()
# logging.warning('~~~~~~~~~')
# logging.warning(sema.__dict__)
#
# for i in range(4):
#     sema.release()
# logging.warning(sema.__dict__)
#
# for i in range(3):
#     sema.acquire()
# logging.warning('~~~~~~~~~~~~')
# logging.warning(sema.__dict__)
# sema.acquire()
# logging.warning('~~~~~~~~~~~~~')
# logging.warning(sema.__dict__)


# import threading
# import logging
# import random
#
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(level=logging.INFO, format=FORMAT)
#
#
# class Conn:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return self.name
#
#
# class Pool:
#     def __init__(self, count: int):
#         self.count = count
#         # 池中是连接对象的列表
#         self.pool = [self._connect('conn-{}'.format(x)) for x in range(count)]
#         self.semaphore = threading.BoundedSemaphore(count)
#
#     def _connect(self, conn_name):
#         # 返回一个名称
#         return Conn(conn_name)
#
#     def get_conn(self):
#         # 从池中拿走一个连接
#         print('---------------')
#         self.semaphore.acquire()
#         print('==============')
#         conn = self.pool.pop()
#         return conn
#
#     def return_conn(self, conn: Conn):
#         # 向池中添加一个连接
#         self.pool.append(conn)
#         self.semaphore.release()
#
#
# # 连接池初始化
# pool = Pool(3)
#
#
# def worker(pool: Pool):
#     conn = pool.get_conn()
#     logging.info(conn)
#     # 模拟使用了一段时间
#     threading.Event().wait(random.randint(1, 4))
#     pool.return_conn(conn)
#
#
# for i in range(6):
#     threading.Thread(target=worker, name='worker-{}'.format(i), args=(pool,)).start()


# import logging
# import datetime
#
#
# logging.basicConfig(level=logging.INFO, format='%(thread)s %(message)s')
# start = datetime.datetime.now()
#
#
# def calc():
#     sum = 0
#     for _ in range(1000000000):
#         sum += 1
#
#
# calc()
# calc()
# calc()
# calc()
# calc()
#
# delta = (datetime.datetime.now() - start).total_seconds()
# logging.info(delta)


# import threading
# import logging
# import datetime
#
#
# logging.basicConfig(level=logging.INFO, format='%(thread)s, %(message)s')
# start = datetime.datetime.now()
#
#
# def calc():
#     sum = 0
#     for _ in range(1000000000):
#         sum += 1
#
#
# t1 = threading.Thread(target=calc)
# t2 = threading.Thread(target=calc)
# t3 = threading.Thread(target=calc)
# t4 = threading.Thread(target=calc)
# t5 = threading.Thread(target=calc)
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
#
# delta = (datetime.datetime.now() - start).total_seconds()
# logging.info(delta)

# 12176 339.561302
# 3632, 378.274209




























































































































