import re
import datetime
from queue import Queue
import threading
from pathlib import Path
from user_agents import parse

# line = '123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] "GET /o2o/media.html?menu=3 HTTP/1.1" 200 8642 "-" ' \
#        '"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"'

ops = {'datetime': lambda x: datetime.datetime.strptime(x, '%d/%b/%Y:%H:%M:%S %z'),
       'status': int, 'length': int, 'useragent': lambda ua: parse(ua)
       }
pattern = '(?P<remote>[\d.]{7,15}) - - \[(?P<datetime>[^\[\]]*)\]' \
          ' "(?P<method>[\w]+) (?P<url>.+) (?P<protocol>[\w/\d.]+)"' \
          ' (?P<status>[\d]+) (?P<length>[\d]+) .+ "(?P<useragent>[^"]*)"'

regex = re.compile(pattern)


def extract(line: str):
    matcher = regex.match(line)
    if matcher:
        return {k: ops.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}
    else:
        return None


def load_file(path1, encoding='utf-8'):
    with open(path1, encoding=encoding) as f:
        for line in f:
            fields = extract(line)
            if isinstance(fields, (dict,)):
                yield fields
            else:
                print('No match. {}'.format(fields))


def load(*args, ext='*.log', r=False, encoding='utf-8'):
    for p in args:
        path = Path(p)
        if path.is_dir():
            if isinstance(ext, str):
                ext = [ext]
            for e in ext:
                logs = path.rglob(e) if r else path.glob(e)
                for log in logs:  # log是Path对象,glob返回的是生成器
                    yield from load_file(str(log.absolute()), encoding=encoding)
        elif path.is_file():
            yield from load_file(path.absolute(), encoding=encoding)


#  分析函数、处理函数
# def handler(iterable):
#     return sum(map(lambda x: x['value'], iterable)) / len(iterable)


# 状态码的分析
def status_handler(iterable: list):  # 指的是一个时间段内的数据list(dict)
    status = {}
    for item in iterable:
        key = item['status']
        status[key] = status.get(key, 0) + 1
    total = len(iterable)
    return {k: v/total for k, v in status.items()}


all_browsers = {}


# 浏览器分析
def browser_handler(iterable: list):
    browsers = {}
    for item in iterable:
        ua = item['useragent']

        key = (ua.browser.family, ua.browser.version_string)
        browsers[key] = browsers.get(key, 0) + 1

        all_browsers[key] = all_browsers.get(key, 0) + 1
    return browsers


# 窗口函数
def window(q: Queue, handler, width: int, interval: int):
    """窗口函数

    :param q: 数据源，生成器，用来拿数据
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
            # print(current)
            # current为<class 'datetime.datetime'> 2017-01-01 01:00:00+08:00

        # 每隔interval计算buffer中的数据一次
        # current-start为1:00:00 <class 'datetime.timedelta'>
        # (current-start).total_seconds()为<class 'float'> 3600.0
        if (current-start).total_seconds() >= interval:
            print('--------')
            ret = handler(buffer)
            print('{}'.format(ret))
            # print(threading.current_thread())
            start = current
            # 清除超出width的数据
            buffer = [x for x in buffer if x['datetime'] > current - delta]
            # current - delta为<class 'datetime.datetime'> 2017-01-01 00:59:55+08:00


# 分发器，决定着数据的调度
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
            # data = next(src)  # src是一个生成器  改这里，数据源不同
            for data in src:
                for q in queues:
                    q.put(data)
            print('='*30)
            while True:
                cmd = input('>>>')
                if cmd == 'plot':
                    print(all_browsers)
                    # new_dict = {}
                    # for (k, ver), val in all_browsers.items():
                    #     new_dict[k] = new_dict.get(k, 0) + val
                    print(sorted(all_browsers.items(), key=lambda x: x[-1], reverse=True))

    return reg, run


if __name__ == '__main__':
    s = load('C:/Users/Zoes/Videos/EDU_Python/文档/chapter07/test.log')
    # s = load('C:/Users/Zoes/Videos/EDU_Python/文档/chapter07/access.log')
    reg, run = dispatcher(s)  # s返回的是一个生成器
    reg(status_handler, 10, 5)
    reg(browser_handler, 10, 10)

    # print(threading.current_thread())
    run()

