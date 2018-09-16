import re
import datetime
from pathlib import Path
from queue import Queue
from user_agents import parse
import threading

line = '123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] "GET /o2o/media.html?menu=3 HTTP/1.1" 200 8642 "-" ' \
       '"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"'

pattern = '(?P<remote>[\d\.]{7,})\s-\s-\s\[(?P<datetime>[^\[\]]+)\]\s' \
          '"(?P<method>[\w]+)\s(?P<url>.*)\s(?P<protocol>.*)\s' \
          '(?P<status>[\d]{3})\s(?P<length>\d+)\s"[^"]+"\s"(?P<user_agent>[^"]+)"'

regex = re.compile(pattern)
ops = {'datetime': lambda date: datetime.datetime.strptime(date, '%d/%b/%Y:%H:%M:%S %z'),
       'status': int,
       'length': int
       }


def extract(line: str):
    result = regex.match(line)
    if result:
        return {k: ops.get(k, lambda x: x)(v) for k, v in result.groupdict().items()}


def load_file(path, encoding='utf-8'):
    with open(path, encoding=encoding) as f:
        for line in f:
            fields = extract(line)
            if isinstance(fields, (dict,)):
                yield fields
            else:
                return 'no match {}'.format(fields)


def load(*args, encoding='utf-8', ext='*.log', r=False):
    for p in args:
        path = Path(p)
        if path.is_dir():
            if isinstance(path, str):
                ext = [ext]
            for e in ext:
                logs = path.rglob(e) if r else path.glob(e)  # logs是生成器
                for log in logs:  # log是path对象
                    yield from load_file(str(log.absloute()), encoding=encoding)
        elif path.is_file():
            yield from load_file(path.absolute(), encoding=encoding)


def window(q, handler, width: int, interval: int):
    start = datetime.datetime.strptime('20170101 000000 +0800', '%Y%m%d %H%M%S %z')
    current = datetime.datetime.strptime('20170101 010000 +0800', '%Y%m%d %H%M%S %z')
    buffer = []
    delta = datetime.timedelta(seconds=width - interval)
    while True:
        # 从数据源获取数据
        data = q.get()
        if data:
            buffer.append(data)
            current = data['datetime']
            if (current - start).total_seconds() >= interval:
                ret = handler(buffer)
                print('{}'.format(ret))
                start = current
                # 清除过期的数据
                buffer = [x for x in buffer if x['datetime'] > current - delta]


def status_handler(src):  # list(dict)
    status = {}
    for item in src:
        key = item['status']
        status[key] = status.get(key, 0) + 1
    total = len(src)
    return {k: v/total for k, v in status.items()}


all_browser = {}


def browser_handler(src):
    browsers = {}
    for item in src:
        ua_str = item['user_agent']
        ua = parse(ua_str)
        key = ua.browser.family, ua.browser.version_string
        browsers[key] = browsers.get(key, 0) + 1
        all_browser[key] = all_browser.get(key, 0) + 1
    return browsers


def dispatcher(iterator):
    queues = []
    threading_handler = []

    def reg_fun(handler, width, interval):
        q = Queue()
        t = threading.Thread(target=window, args=(q, handler, width, interval))
        queues.append(q)
        threading_handler.append(t)

    def run():  # 启动线程
        for t in threading_handler:
            t.start()
        while True:
            for data in iterator:
                for q in queues:
                    q.put(data)
            print('-'*30)
            while True:
                cmd = input('>>>')
                if cmd == 'plot':
                    print(all_browser)
                    print(sorted(all_browser.items(), key=lambda x: x[-1], reverse=True))

    return reg_fun, run


if __name__ == '__main__':
    s = load('C:/Users/Zoes/Videos/EDU_Python/文档/chapter07/test.log')
    reg_fun, run = dispatcher(s)
    reg_fun(status_handler, 10, 5)
    reg_fun(browser_handler, 10, 10)
    run()


