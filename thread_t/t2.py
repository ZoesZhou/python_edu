# import threading
# import time
#
#
# def worker():
#     count = 0
#     while True:
#         if count > 5:
#             break
#         time.sleep(1)
#         count += 1
#         print('I am working')
#
#
# class MyThread(threading.Thread):
#     def start(self):
#         print('start------------')
#         super().start()
#
#     def run(self):
#         print('running============')
#         super().run()
#
#
# t = MyThread(target=worker, name='worker')
# t.start()
# # t.run()
# print(t.ident)


# while True:
#     time.sleep(1)
#     if t.is_alive():
#         print('{} {} alive'.format(t.name, t.ident))
#     else:
#         print('{} {} dead'.format(t.name, t.ident))
#         # t.start()
#     break


# import threading
# import time
#
#
# def worker():
#     count = 0
#     while True:
#         if count > 5:
#             break
#         time.sleep(1)
#         count += 1
#         print('I am working')
#         print(threading.current_thread().name, threading.current_thread().ident)
#
#
# class MyThread(threading.Thread):
#     def start(self):
#         print('start------------')
#         super().start()
#
#     def run(self):
#         print('running============')
#         super().run()
#
#
# t1 = MyThread(target=worker, name='worker1')
# t2 = MyThread(target=worker, name='worker2')
# t1.start()
# t2.start()
# t1.run()
# t2.run()


# import threading
#
#
# def worker():
#     for x in range(100):
#         print('{} is running.\n'.format(threading.current_thread().name), end='')
#
#
# for x in range(1, 5):
#     name = 'worker{}'.format(x)
#     t = threading.Thread(name=name, target=worker)
#     t.start()


# import threading
# import logging
#
#
# def worker():
#     for x in range(100):
#         logging.warning('{} is running'.format(threading.current_thread().name))
#
#
# for x in range(1, 5):
#     name = 'worker{}'.format(x)
#     t = threading.Thread(name=name, target=worker)
#     t.start()


import threading
import time


def foo():
    time.sleep(5)
    for i in range(20):
        print(i)


t = threading.Thread(target=foo, daemon=False)
t.start()

print('Main Thread Exiting')











