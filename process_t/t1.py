# import multiprocessing
# import datetime
#
#
# def calc(i):
#     sum = 0
#     for _ in range(1000000000):
#         sum += 1
#     print(sum)
#
#
# if __name__ == '__main__':
#     start = datetime.datetime.now()
#     ps = []
#     for i in range(2):
#         p = multiprocessing.Process(target=calc, args=(i,), name='calc={}'.format(i))
#         ps.append(p)
#         p.start()
#     for p in ps:
#         p.join()
#
#     delta = (datetime.datetime.now() - start).total_seconds()
#     print(delta)
#     print('end=====')


# import multiprocessing
# import datetime
# import logging
#
# logging.basicConfig(level=logging.INFO, format='%(process)d %(processName)s %(thread)d %(message)s')
#
#
# def calc():
#     sum = 0
#     for _ in range(10000000):
#         sum += 1
#     return sum
#
#
# if __name__ == '__main__':
#     start = datetime.datetime.now()
#     pool = multiprocessing.Pool(2)
#     for i in range(2):
#         pool.apply_async(calc, callback=lambda x: logging.info(x))
#     pool.close()
#     pool.join()
#     delta = (datetime.datetime.now() - start).total_seconds()
#     print(delta)


# import threading
# from concurrent import futures
# import logging
# import time
# FORMAT = '%(processName)s %(process)d %(thread)d %(message)s'
# logging.basicConfig(level=logging.INFO, format=FORMAT)
#
#
# def worker(n):
#     logging.info('begin to work{}'.format(n))
#     time.sleep(2)
#     logging.info('finished{}'.format(n))
#
#
# executor = futures.ThreadPoolExecutor(max_workers=3)
# # executor = futures.ProcessPoolExecutor(max_workers=3)
# fs = []
# for i in range(3):
#     future = executor.submit(worker, i)
#     fs.append(future)
#
# while True:
#     time.sleep(2)
#     logging.info(threading.enumerate())
#     flag = True
#     for f in fs:  # 判断是否还有未完成的任务
#         flag = flag and f.done()
#     if flag:
#         logging.info('=========')
#         executor.shutdown()
#         for f in fs:
#             logging.info('{} result = {}'.format(f, f.result()))
#         break
#
# logging.info('end')


import threading
from concurrent import futures
import logging
import time
FORMAT = '%(processName)s %(process)d %(thread)d %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker(n):
    logging.info('begin to work{}'.format(n))
    time.sleep(2)
    logging.info('finished{}'.format(n))


if __name__ == '__main__':
    executor = futures.ProcessPoolExecutor(max_workers=3)
    with executor:
        fs = []
        for i in range(3):
            future = executor.submit(worker, i)
            fs.append(future)

        while True:
            time.sleep(2)
            logging.info(threading.enumerate())
            flag = True
            for f in fs:
                logging.info(f.done())
                flag = flag and f.done()

            if flag:
                logging.info(threading.enumerate())
                break

































































































