import random
import datetime
import time
from queue import Queue
import threading


# # 一段时间内产生了数据，等了一段固定时间取数据来计算平均值
# def source(seconds=1):
#     while True:
#         yield {'datetime': datetime.datetime.now(), 'value': random.randint(1, 100)}
#         time.sleep(seconds)
#
#
# # 攒一批数据
# s = source()
# items = [next(s) for _ in range(3)]
# print(items)
#
#
# # 处理函数，送入一批数据计算一个结果
# def handler(iterable):
#     return sum(map(lambda item: item['value'], iterable)) / len(iterable)
#
#
# print('{:.2f}'.format(handler(items)))


# 将上面的获取数据的程序扩展为window函数。使用重叠的方案
# 有时区的时间(aware)和没有时区的时间(naive)是不能直接相加减的
def source(second=1):
    """生成数据"""
    while True:
        yield {'datetime': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))),
               'value': random.randint(1, 100)
               }
        time.sleep(second)


def window(q: Queue, handler, width: int, interval: int):
    """窗口函数

    :param iterable: 数据源，生成器，用来拿数据
    :param handler: 数据处理函数
    :param width: 时间窗口宽度，秒
    :param interval: 处理时间间隔，秒
    :return:
    """
    # datetime构造器
    start = datetime.datetime.strptime('20170101 000000 +0800', '%Y%m%d %H%M%S %z')
    current = datetime.datetime.strptime('20170101 010000 +0800', '%Y%m%d %H%M%S %z')
    buffer = []  # 窗口中的待计算数据
    delta = datetime.timedelta(seconds=width-interval)
    # delta <class 'datetime.timedelta'> 0:00:05
    while True:
        # 从数据源获取数据
        data = q.get()  # 阻塞的  # next(iterable)
        if data:
            buffer.append(data)  # 存入临时缓冲等待计算
            current = data['datetime']
            print(current)
            # current为<class 'datetime.datetime'> 2017-01-01 01:00:00+08:00

        # 每隔interval计算buffer中的数据一次
        # current-start为1:00:00 <class 'datetime.timedelta'>
        # (current-start).total_seconds()为<class 'float'> 3600.0
        if (current-start).total_seconds() >= interval:
            print('--------')
            ret = handler(buffer)
            print('{:.2f}'.format(ret))
            print(threading.current_thread())
            start = current
            # 清除超出width的数据
            buffer = [x for x in buffer if x['datetime'] > current - delta]
            # current - delta为<class 'datetime.datetime'> 2017-01-01 00:59:55+08:00


def handler(iterable):
    return sum(map(lambda x: x['value'], iterable)) / len(iterable)


# window(source(), handler, 10, 5)


def dispatcher(src):
    handlers = []  # 线程对象，但是里面其实是不同的handler
    queues = []

    def reg(handler, width, interval):  # 数据是谁？
        q = Queue()
        t = threading.Thread(target=window, args=(q, handler, width, interval))

        queues.append(q)
        handlers.append(t)

    def run():
        for t in handlers:
            t.start()
        while True:
            data = next(src)  # 改这里，数据源不同
            for q in queues:
                q.put(data)

    return reg, run


reg, run = dispatcher(source())

reg(handler, 10, 5)

print(threading.current_thread())
run()

