# import socket
#
# sock = socket.socket()  # 创建socket对象
# ip = '127.0.0.1'
# port = 9999
# addr = (ip, port)
#
# sock.bind(addr)  # 绑定地址和端口
#
# sock.listen()  # 开始监听
#
# # 阻塞直到和客户端成功建立连接，返回新的socket对象和客户端地址
# s, info = sock.accept()
# print(1, s)
# print(2, info)
#
# # 使用缓冲获取数据
# data = s.recv(1024)  # 阻塞，等待client发送数据
# print(3, data, '---------')
# # 发送给server端
# msg = 'your msg={}'.format(data.decode())
# s.send(msg.encode())
# sock.close()


# import socket
#
# server = socket.socket()
# server.bind(('127.0.0.1', 9999))
# server.listen()
# s1, _ = server.accept()
# data = s1.recv(1024)
# print(data)
# msg = 'msg = {}'.format(data.decode())
# s1.send(msg.encode())
#
# s2, _ = server.accept()
# d = s2.recv(1024)
# print(d)
# m = 'msg = {}'.format(d.decode())
# s2.send(m.encode())
# server.close()


import socket
import threading
import logging

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.FileHandler('C:/Users/Zoes/Videos/EDU_Python/文档/chapter12网络编程/test.log')
fmt = logging.Formatter(FORMAT)
handler.setFormatter(fmt)
log.addHandler(handler)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.socket = socket.socket()
        self.addr = ip, port
        self.clients = {}  # 客户端
        self.event = threading.Event()

    def start(self):
        self.socket.bind(self.addr)
        self.socket.listen()
        # self.accept()  # 等待连接时会阻塞主线程
        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):  # 多人连接
        while not self.event.is_set():
            sock, client = self.socket.accept()
            f = sock.makefile('rw')
            self.clients[client] = f  # 存储连接的客户端
            # self.recv(sock)  # recv一直在循环，第二次连接建立不了
            threading.Thread(target=self.recv, args=(f, client)).start()

    def recv(self, f, client):  # 接受客户端数据
        while not self.event.is_set():
            # data = sock.recv(1024)  # 阻塞到数据到来
            data = f.readline()
            log.info(data)
            if data.strip() == 'quit':
                self.clients.pop(client)  # 客户端主动断开连接
                f.close()  # 释放资源
                break
            self.sends(data)

    def sends(self, data):
        msg = 'msg={}'.format(data)
        for s in self.clients.values():
            s.write(msg)
            s.flush()

    def stop(self):  # 停止服务
        for s in self.clients.values():
            s.close()
        self.socket.close()
        self.event.set()


cs = ChatServer()
cs.start()

while True:
    cmd = input('>>>')
    if cmd.strip() == 'quit':
        cs.stop()
        break
    print(threading.enumerate())

























































































