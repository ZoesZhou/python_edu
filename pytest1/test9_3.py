import threading
import time
from queue import Queue


# def add(x, y):
#     print('entering this thread.')
#     time.sleep(2)
#     print(x + y)
#     print('='*30)
#
#
# t = threading.Thread(target=add, args=(4, 5))
# t.start()
# print('*'*30)


# q = Queue()
# def add(x, y):
#     while True:
#         print('~'*30)
#         cmd = q.get()  # 卡住了
#         print('='*30)
#
#
# t = threading.Thread(target=add, args=(4, 5))
# t.start()
# print('*'*30)
# while True:
#     cmd = input('<><><')
#     if cmd == '':
#         break
#     if cmd:
#         q.put(cmd)
#         print('+'*30)


# from pathlib import Path
#
#
# def load(*args, encoding='utf-8', ext='*.log', r=False):
#     for p in args:
#         path = Path(p)
#         if path.is_dir():
#             if isinstance(ext, str):
#                 ext = [ext]
#             for e in ext:
#                 logs = path.rglob(e) if r else path.glob(e)
#                 for log in logs:  # log是Path对象,glob返回的是生成器
#                     with log.open(encodling=encoding) as f:
#                         for line in f:
#                             pass
#         elif path.is_file():
#             pass


from user_agents import parse

ua_str = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36" \
     " (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36" \
     " SE 2.X MetaSr 1.0"

ua = parse(ua_str)
print(ua, type(ua))
print(ua.browser)
print(ua.browser.family, ua.browser.version_string)