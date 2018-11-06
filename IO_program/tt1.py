# import socket
#
# server = socket.socket(type=socket.SOCK_DGRAM)
# server.bind(('127.0.0.1', 9999))  # 立即绑定一个udp端口
# data= server.recv(1024)  # 阻塞等待数据
# print(data)
# data = server.recvfrom(1024)
# print(data)
# server.sendto(b'4', ('127.0.0.1', 10000))
# server.close()


# import socket
#
#
# client = socket.socket(type=socket.SOCK_DGRAM)
# raddr = ('127.0.0.1', 9999)
#
# client.connect(raddr)
# client.sendto(b'o', raddr)
# client.send(b'9')
# data = client.recv(1024)
# print(data)
# data = client.recvfrom(1024)
# print(data)
# client.close()


# import socket
# import logging
# import threading
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class ChatUDPServer:
#     def __init__(self, ip='127.0.0.1', port=9999):
#         self.sock = socket.socket(type=socket.SOCK_DGRAM)
#         self.addr = (ip, port)
#         self.event = threading.Event()
#         self.clients = set()
#
#     def start(self):
#         self.sock.bind(self.addr)
#         threading.Thread(target=self.recv, name='recv').start()
#
#     def recv(self):
#         while not self.event.is_set():
#             data, raddr = self.sock.recvfrom(1024)  # 阻塞接受数据
#             if data.strip() == b'quit':
#                 if raddr in self.clients:  # 有可能发来的数据不再clients中
#                     self.clients.remove(raddr)
#                 logging.info('{} leaving'.format(raddr))
#                 continue
#             self.clients.add(raddr)
#             msg = '{} from {}:{}'.format(data.decode(), *raddr)
#             logging.info(msg)
#             msg = msg.encode()
#             for c in self.clients:
#                 self.sock.sendto(msg, c)  # 不保证对方能够收到
#
#     def stop(self):
#         for c in self.clients:
#             self.sock.sendto(b'bye', c)
#         self.sock.close()
#         self.event.set()
#
#
# def main():
#     cs = ChatUDPServer()
#     cs.start()
#     while True:
#         cmd = input('>>>')
#         if cmd.strip() == 'quit':
#             cs.stop()
#             break
#         print(threading.enumerate())
#         print(cs.clients)
#
#
# if __name__ == '__main__':
#     main()


# import socket
# import threading
# import logging
# import datetime
#
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class ChatUDPServer:
#     def __init__(self, ip='127.0.0.1', port=9999, interval=10):
#         self.sock = socket.socket(type=socket.SOCK_DGRAM)
#         self.addr = (ip, port)
#         self.event = threading.Event()
#         self.clients = {}  # 记录客户端
#         self.interval = interval
#
#     def start(self):
#         self.sock.bind(self.addr)
#         threading.Thread(target=self.recv, name='recv').start()
#
#     def recv(self):
#         while not self.event.is_set():
#             data, raddr = self.sock.recvfrom(1024)  # 阻塞接受数据
#             local_keys = set()
#             current = datetime.datetime.now().timestamp()
#             if data.strip() == b'^hb^':  # 心跳信息
#                 self.clients[raddr] = current
#                 continue
#             elif data.strip() == b'quit':
#                 if raddr in self.clients.keys():
#                     self.clients.pop(raddr)
#                 logging.info('{} leaving'.format(raddr))
#                 continue
#             self.clients[raddr] = current  # 有信息来就更新时间
#             msg = '{} from {}:{}'.format(data.decode(), *raddr)
#             logging.info(msg)
#             msg = msg.encode()
#             # 在发送信息的同时，删除超时的客户端
#             for c, v in self.clients.items():
#                 if current - v > self.interval:
#                     local_keys.add(c)  # 字典在遍历时不能删除
#                 else:  # 把要删除的地址暂存在集合里
#                     self.sock.sendto(msg, c)
#             for c in local_keys:  # 删除超时的客户端
#                 self.clients.pop(c)
#
#     def stop(self):
#         for c, v in self.clients.items():
#             self.sock.sendto(b'bye', c)
#         self.sock.close()
#         self.event.set()
#
#
# def main():
#     cs = ChatUDPServer()
#     cs.start()
#     while True:
#         cmd = input('>>>')
#         if cmd.strip() == 'quit':
#             cs.stop()
#             break
#         print(threading.enumerate())
#         print(cs.clients)
#
#
# if __name__ == '__main__':
#     main()


# import socket
# import logging
# import threading
# import datetime
#
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class ChatUDPServer:
#     def __init__(self, ip='127.0.0.1', port=9999, interval=10):
#         self.sock = socket.socket(type=socket.SOCK_DGRAM)
#         self.address = ip, port
#         self.event = threading.Event()
#         self.clients = {}
#         self.interval = interval
#
#     def start(self):
#         self.sock.bind(self.address)
#         threading.Thread(target=self.receive, name='receive').start()
#
#     def receive(self):
#         while not self.event.is_set():
#             data, raddr = self.sock.recvfrom(1024)  # 阻塞接收数据
#             local_keys = set()  # 清理超时
#             current = datetime.datetime.now().timestamp()  # float
#             if data.strip() == b'^hb^':  # 心跳信息
#                 self.clients[raddr] = current
#                 print('^^^^^hb', raddr)
#                 continue
#             if data.strip() == b'quit':
#                 if data in self.clients:
#                     self.clients.pop(raddr)
#                 continue
#             self.clients[raddr] = current
#             msg = '{} from {}:{}'.format(data.decode(), *raddr)
#             logging.info(msg)
#             msg = msg.encode()
#             for c, v in self.clients.items():
#                 if current - v > self.interval:
#                     local_keys.add(c)
#                 else:
#                     self.sock.sendto(msg, c)
#             for c in local_keys:
#                 self.clients.pop(c)
#
#     def stop(self):
#         for c, v in self.clients.items():
#             self.sock.sendto(b'bye', c)
#         self.sock.close()
#         self.event.set()
#
#
# def main():
#     cs = ChatUDPServer()
#     cs.start()
#     while True:
#         cmd = input('>>>')
#         if cmd.strip() == 'quit':
#             cs.stop()
#             break
#         print(threading.enumerate())
#         print(cs.clients)
#
#
# if __name__ == '__main__':
#     main()


# import socketserver
#
#
# class ChatHandler(socketserver.BaseRequestHandler):
#     clients = {}
#
#     def handle(self):
#         while True:
#             data = self.request.recv(1024)
#             self.clients[self.client_address] = self.request
#             if data.strip() == b'quit' or data == b'':
#                 for c, v in self.clients.items():
#                     self.clients.pop(c)
#                     v.close()
#                     break
#             for v in self.clients.values():
#                 v.send(data)
#             # print(1, data)
#
#
# address = ('127.0.0.1', 9999)
# ch = socketserver.ThreadingTCPServer(address, ChatHandler)
# ch.serve_forever()
# print('------')
# ch.server_close()
# print('========')


# from socketserver import ThreadingTCPServer, BaseRequestHandler
# import threading
# import sys
#
#
# class EchoHandler(BaseRequestHandler):
#     def setup(self):
#         super().setup()
#         self.event = threading.Event()
#
#     def finish(self):
#         super().finish()
#         self.event.set()
#
#     def handle(self):
#         super().handle()
#         while not self.event.is_set():
#             data = self.request.recv(1024).decode()
#             msg = '{} {}'.format(self.client_address, data).encode()
#             self.request.send(msg)
#         print('End')
#
#
# addr = ('127.0.0.1', 9999)
# server = ThreadingTCPServer(addr, EchoHandler)
# server.handle_request()


# import socket
# import selectors
#
#
# selector = selectors.DefaultSelector()
# server = socket.socket()
# server.bind(('127.0.0.1', 9999))
# server.listen()
#
#
# def accept(sock: socket.socket):
#     conn, raddr = sock.accept()
#     key = selector.register(conn, selectors.EVENT_READ, data=recv)
#     print(conn)
#     print(raddr)
#     conn.send(b'hello, client')
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#
#
# def recv(conn: socket.socket):
#     data = conn.recv(1024)
#     print('-'*30)
#     msg = 'msg = {}'.format(data.decode())
#     conn.send(msg.encode())
#     print('-'*30)
#
#
# key = selector.register(server, selectors.EVENT_READ, data=accept)
# print(1, key)
# print(2, key.data)
#
# while True:
#     print('-'*30)
#     events = selector.select()  # blocking
#     for key, mask in events:
#         print(key)
#         print(key.data)
#         print(mask)
#         key.data(key.fileobj)


# import selectors
# import socket
# import threading
#
# # 构造缺省性能最优selector
# selector = selectors.DefaultSelector()
# # 创建Tcp Server
# server = socket.socket()
# server.bind(('127.0.0.1', 9999))
# server.listen()
# server.setblocking(False)  # 非阻塞
#
#
# # 回调函数，自己定义形参
# def accept(sock: socket.socket):  # accept
#     print('+++++++++++++++++++')
#     conn, raddr = sock.accept()
#     conn.setblocking(False)
#     key = selector.register(conn, selectors.EVENT_READ, data=recv)
#     print(1, conn)
#     print(2, raddr)
#     conn.send(b'hello, client')
#
#
# # 回调函数
# def recv(conn: socket.socket):
#     data = conn.recv(1024)
#     msg = 'msg={}'.format(data.decode())
#     print(msg, '~~~~~~~~~~~~~')
#     conn.send(msg.encode())
#
#
# # 注册文件对象sock关注读事件，返回SelectorKey
# # 将sock、关注事件、data都绑定到key实例属性上
# key = selector.register(server, selectors.EVENT_READ, data=accept)
# print(key)
# event = threading.Event()
#
#
# def select():
#     while not event.is_set():
#         print('-'*30)
#         # 开始监视，等到有文件对象监控事件产生
#         # 返回一个列表[(key,selectors.EVENT_READ)]
#         data = selector.select()  # blocking,只要有一个就绪，就不阻塞
#         for key, mask in data:
#             print(key)
#             print(key.data.__name__)
#             print(mask)
#             key.data(key.fileobj)
#         # print(data)
#
#
# threading.Thread(target=select, name='select').start()
#
#
# def main():
#     while not event.is_set():
#         cmd = input('>>>')
#         if cmd.strip() == 'quit':
#             event.set()
#             fobjs = []
#             print('{}'.format(list(selector.get_map().items())))
#             for fd, key in selector.get_map().items():
#                 print(fd, key)
#                 print(key.fileobj)
#                 fobjs.append(key.fileobj)
#
#             for fobj in fobjs:
#                 selector.unregister(fobj)
#                 fobj.close()
#             selector.close()
#         print(list(selector.get_map().items()))
#         print(list(selector.get_map().keys()))
#         print(list(selector.get_map().values()))
#
#
# if __name__ == '__main__':
#     main()


# # IO多路复用，read
# import socket
# import threading
# import logging
# import selectors
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class ChatServer:
#     def __init__(self, ip='127.0.0.1', port=9999):
#         self.addr = ip, port
#         self.event = threading.Event()
#         self.sock = socket.socket()
#         self.selector = selectors.DefaultSelector()
#
#     def start(self):
#         self.sock.bind(self.addr)
#         self.sock.listen()
#         self.sock.setblocking(False)
#         self.selector.register(self.sock, selectors.EVENT_READ, data=self.accept)
#         threading.Thread(target=self.select, name='select', daemon=True).start()
#
#     def select(self):
#         while not self.event.is_set():
#             print('-'*30)
#             # 开始监视，等到有文件对象监控事件产生
#             # 返回一个列表[(key,selectors.EVENT_READ)]
#             data = self.selector.select()  # blocking,只要有一个就绪，就不阻塞
#             for key, mask in data:
#                 print(key)
#                 print(mask)
#                 key.data(key.fileobj)
#
#     def accept(self, sock: socket.socket):
#         conn, raddr = sock.accept()
#         conn.setblocking(False)
#         self.selector.register(conn, selectors.EVENT_READ, data=self.recv)
#
#     def recv(self, conn: socket.socket):
#         data = conn.recv(1024)
#         msg = 'msg={}'.format(data.decode()).encode()
#         logging.info(data)
#         if data.strip() == b'quit' or data == b'':
#             self.selector.unregister(conn)
#             conn.close()
#             return
#         for key in self.selector.get_map().values():
#             if key.data == self.recv:
#                 print(11, id(key.data))
#                 print(12, id(self.recv))
#                 key.fileobj.send(msg)
#
#     def stop(self):
#         self.event.set()
#         fobjs = []
#         print('{}'.format(list(self.selector.get_map().items())))
#         for fd, key in self.selector.get_map().items():
#             print(fd, key)
#             print(key.fileobj)
#             fobjs.append(key.fileobj)
#
#         for fobj in fobjs:
#             self.selector.unregister(fobj)
#             fobj.close()
#         self.selector.close()
#
#
# def main():
#     cs = ChatServer()
#     cs.start()
#     while True:
#         cmd = input('>>>')
#         if cmd.strip() == 'quit':
#             cs.stop()
#             break
#         print(threading.enumerate())
#
#
# if __name__ == '__main__':
#     main()


# 同时监听读写
# import socket
# import threading
# import selectors
# import logging
# from queue import Queue
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class ChatServer:
#     def __init__(self, ip='127.0.0.1', port=9999):
#         self.sock = socket.socket()
#         self.addr = ip, port
#         self.event = threading.Event()
#         self.selector = selectors.DefaultSelector()  # 创建selector
#
#     def start(self):
#         self.sock.bind(self.addr)
#         self.sock.listen()
#         self.sock.setblocking(False)  # 不阻塞
#         self.selector.register(self.sock, selectors.EVENT_READ, data=self.accept)
#         threading.Thread(target=self.select, name='select', daemon=True).start()
#
#     def select(self):
#         while not self.event.is_set():
#             # 开始监听，等到某文件对象被监控的事件产生，返回(key,mask)
#             events = self.selector.select()  # 阻塞，直到有一个就绪
#             for key, mask in events:
#                 # if key.data == self.accept:
#                 if callable(key.data):  # self.accept
#                     key.data(key.fileobj)
#                 else:  # 元组(self.handel,Queue())
#                     key.data[0](key, mask)  # 使用key把所有需要的都传过去
#
#     def accept(self, sock: socket.socket):
#         conn, raddr = sock.accept()
#         conn.setblocking(False)
#         # 注册，监听每一个与客户端的连接的socket对象
#         self.selector.register(conn, selectors.EVENT_READ | selectors.EVENT_WRITE, data=(self.handle, Queue()))
#
#     def handle(self, key: selectors.SelectorKey, mask):  # 接受客户端数据
#         if mask & selectors.EVENT_READ:  # 0001与结果是1或0
#             conn = key.fileobj
#             data = conn.recv(1024)
#             logging.info(data)
#             msg = '{}'.format(data.decode()).encode()
#             if data.strip() == b'quit' or data == b'':
#                 self.selector.unregister(conn)
#                 conn.close()
#                 return
#             # 群发
#             for key in self.selector.get_map().values():
#                 if isinstance(key.data, tuple):
#                     key.data[1].put(msg)
#         if mask & selectors.EVENT_WRITE:  # 0010与结果是2或0
#             # 因为写一直就绪，mask为2，所以一直可以写，从而导致select()不断循环，如同不阻塞一样
#             if not key.data[1].empty():
#                 key.fileobj.send(key.data[1].get())
#
#     def stop(self):
#         self.event.set()
#         fobjs = []
#         for fd, key in self.selector.get_map().items():
#             fobjs.append(key.fileobj)
#         for fobj in fobjs:
#             self.selector.unregister(fobj)
#             fobj.close()
#         self.selector.close()
#
#
# def main():
#     cs = ChatServer()
#     cs.start()
#     while True:
#         cmd = input('>>>>')
#         if cmd.strip() == 'quit':
#             cs.stop()
#             break
#         print(threading.enumerate())
#
#
# if __name__ == '__main__':
#     main()


# import selectors
# import threading
# import socket
# import logging
# import datetime
# from queue import Queue
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class ChatServer:
#     def __init__(self, ip='127.0.0.1', port=9999):
#         self.sock = socket.socket()
#         self.addr = ip, port
#         self.event = threading.Event()
#         self.selector = selectors.DefaultSelector()
#
#     def start(self):
#         self.sock.bind(self.addr)
#         self.sock.listen()
#         self.sock.setblocking(False)
#         self.selector.register(self.sock, selectors.EVENT_READ, data=self.accept)
#         threading.Thread(target=self.select, name='select', daemon=True).start()
#
#     def select(self):
#         while not self.event.is_set():
#             events = self.selector.select()
#             for key, mask in events:
#                 if callable(key.data):
#                     key.data(key.fileobj)
#                 else:
#                     key.data[0](key, mask)
#
#     def accept(self, sock: socket.socket):
#         conn, raddr = sock.accept()
#         conn.setblocking(False)
#         self.selector.register(conn, selectors.EVENT_READ | selectors.EVENT_WRITE, (self.handle, Queue()))
#
#     def handle(self, key: selectors.SelectorKey, mask):
#         if mask & selectors.EVENT_READ:
#             sock = key.fileobj
#             data = sock.recv(1024)
#             logging.info('{}'.format(data))
#             if data.strip() == b'quit' or data == b'':
#                 self.selector.unregister(sock)
#                 sock.close()
#                 return
#             msg = '{:%Y/%m/%d %H:%M:%S} {}:{}\n{}\n'.format(datetime.datetime.now(),
#                                                             *sock.getpeername(), data.decode())
#             logging.info(msg)
#             msg = msg.encode()
#             for key in self.selector.get_map().values():
#                 if isinstance(key.data, tuple):
#                     key.data[1].put(msg)
#         if mask & selectors.EVENT_WRITE:
#             if not key.data[1].empty():
#                 key.fileobj.send(key.data[1].get())
#
#     def stop(self):
#         self.event.set()
#         fobjs = []
#         for fd, key in self.selector.get_map().items():
#             fobjs.append(key.fileobj)
#         for fobj in fobjs:
#             self.selector.unregister(fobj)
#             fobj.close()
#         self.selector.close()
#
#
# def main():
#     cs = ChatServer()
#     cs.start()
#     while True:
#         cmd = input('>>>')
#         if cmd.strip() == 'quit':
#             logging.info('quit')
#             cs.stop()
#             break
#         print(threading.enumerate())
#
#
# if __name__ == '__main__':
#     main()