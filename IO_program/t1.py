# import socket
#
# server = socket.socket()
#
# ip = '127.0.0.1'
# port = 9999
# addr = (ip, port)
# server.bind(addr)
#
# server.listen()
#
# s, info = server.accept()
# print(s)
# print(info)
#
# data = s.recv(1024)
# print(data)
#
# msg = 'your msg = {}'.format(data.decode())
# s.send(msg.encode())
# server.close()


# import logging
# import threading
# import socket
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# log = logging.getLogger(__name__)
# log.setLevel(logging.INFO)
# handler = logging.FileHandler('C:/Users/Zoes/Videos/EDU_Python/文档/chapter12网络编程/test.log')
# fmt = logging.Formatter(FORMAT)
# handler.setFormatter(fmt)
# log.addHandler(handler)
#
#
# class ChatServer:
#     def __init__(self, ip='127.0.0.1', port=9999):
#         self.sock = socket.socket()  # 创建socket对象
#         self.address = ip, port
#         self.clients = {}
#         self.event = threading.Event()
#
#     def start(self):
#         self.sock.bind(self.address)  # 绑定地址和端口
#         self.sock.listen()  # 开始监听
#         threading.Thread(target=self.accepts).start()  # 阻塞，开启线程
#
#     def accepts(self):  # 多个连接
#         while not self.event.is_set():
#             sock, address = self.sock.accept()
#             self.clients[address] = sock  # 收集连接的客户端
#             threading.Thread(target=self.receive, args=(sock, address)).start()
#
#     def receive(self, sock: socket.socket, client):  # 等待客户端发送数据
#         while not self.event.is_set():
#             data = sock.recv(1024)  # 接受客户端发来的数据
#             log.info(data)
#             print(sock.getpeername())
#             print(sock.getsockname())
#             if data.strip() == b'quit' or data == b'':
#                 self.clients.pop(client)  # 客户端自己断开连接，删除客户端信息
#                 sock.close()  # 释放资源
#                 break
#             msg = 'msg={}'.format(data).encode()
#             for s in self.clients.values():  # 发送信息给所有客户端
#                 s.send(msg)
#
#     def stop(self):  # 停止服务
#         for c in self.clients.values():
#             c.close()
#         self.sock.close()
#         self.event.set()
#
#
# cs = ChatServer()
# cs.start()
#
# while True:
#     cmd = input('>>>')
#     if cmd.strip() == 'quit':
#         cs.stop()
#         break
#     # print(threading.enumerate())


# import socket
# import threading
#
# sockserver = socket.socket()
# ip = '127.0.0.1'
# port = 9999
# addr = (ip, port)
# sockserver.bind(addr)
# sockserver.listen()
# print('-'*30)
# s, _ = sockserver.accept()
# print(s)
# f1 = s.makefile(mode='rw')
#
# print(f1)
#
#
# def recv(f):
#     while True:
#         # line = f1.read(10)
#         line = f.readline()
#         print('-'*30)
#         print(line)
#         if line.strip() == 'quit':
#             break
#         f.write('return your msg:{}'.format(line))
#     # f1.flush()
#
#
# t = threading.Thread(target=recv, args=(f1,))
# t.start()
# t.join()
# sockserver.close()


# import logging
# import threading
# import socket
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# log = logging.getLogger(__name__)
# log.setLevel(logging.INFO)
# handler = logging.FileHandler('C:/Users/Zoes/Videos/EDU_Python/文档/chapter12网络编程/test.log')
# fmt = logging.Formatter(FORMAT)
# handler.setFormatter(fmt)
# log.addHandler(handler)
#
#
# class CharServer:
#     def __init__(self, ip='127.0.0.1', port=9999):
#         self.sock = socket.socket()
#         self.address = (ip, port)
#         self.event = threading.Event()
#         self.clients = {}
#
#     def start(self):
#         self.sock.bind(self.address)
#         self.sock.listen()
#         threading.Thread(target=self.accepts, name='accept').start()
#
#     def accepts(self):
#         while not self.event.is_set():
#             sock, addr = self.sock.accept()
#             file = sock.makefile(mode='rw')
#             self.clients[addr] = file
#             threading.Thread(target=self.receive, args=(sock, file, addr)).start()
#
#     def receive(self, sock, f, client):
#         while not self.event.is_set():
#             # data = sock.recv(1024)
#             data = f.readline()
#             log.info(data)
#             if data.strip() == 'quit':
#                 self.clients.pop(client)
#                 sock.close()
#                 f.close()
#                 break
#             msg = 'msg={}'.format(data)
#             for s in self.clients.values():
#                 s.write(msg)
#                 s.flush()
#
#     def stop(self):
#         for s in self.clients.values():
#             s.close()
#         self.sock.close()
#         self.event.set()
#
#
# cs = CharServer()
# cs.start()
#
# while True:
#     cmd = input('>>>')
#     if cmd == 'quit':
#         cs.stop()
#         break
#     print(threading.enumerate())


import logging
import threading
import socket
import datetime

FORMAT = '%(asctime)s %(thread)d %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.FileHandler('C:/Users/Zoes/Videos/EDU_Python/文档/chapter12网络编程/test.log')
fmt = logging.Formatter(FORMAT)
handler.setFormatter(fmt)
log.addHandler(handler)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.sock = socket.socket()
        self.addr = ip, port
        self.clients = {}
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self.accepts, name='accept').start()

    def accepts(self):
        while not self.event.is_set():
            sock, addr = self.sock.accept()
            f = sock.makefile(mode='rw')
            self.clients[addr] = f
            threading.Thread(target=self.receive, args=(f, addr)).start()

    def receive(self, f, client):
        while not self.event.is_set():
            try:
                data = f.readline()
            except Exception as e:
                log.error(e)
                data = 'quit'
            msg = data.strip()
            if msg == 'quit':
                self.clients.pop(client)
                f.close()
                log.info('{} quit'.format(client))
                break
            msg = '{:%Y/%m/%d %H:%M:%S} {}:{}\n{}\n'.format(datetime.datetime.now(), *client, data)
            log.info(msg)
            for s in self.clients.values():
                s.write(msg)
                s.flush()

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event.set()


def main():
    cs = ChatServer()
    cs.start()
    while True:
        cmd = input('>>>')
        if cmd == 'quit':
            cs.stop()
            break
        log.info(threading.enumerate())


if __name__ == '__main__':
    main()



































































