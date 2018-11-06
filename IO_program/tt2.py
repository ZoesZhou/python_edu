# import socket
# import threading
# import logging
#
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class ChatUDPClient:
#     def __init__(self, ip='127.0.0.1', port=9999):
#         self.sock = socket.socket(type=socket.SOCK_DGRAM)
#         self.addr = (ip, port)
#         self.event = threading.Event()
#
#     def start(self):
#         self.sock.connect(self.addr)  # 占用本地地址和端口，设置远端地址和端口
#         threading.Thread(target=self.recv, name='recv').start()
#
#     def recv(self):
#         while not self.event.is_set():
#             data, raddr = self.sock.recvfrom(1024)
#             msg = '{} from {}:{}'.format(data.decode(), *raddr)
#             logging.info(msg)
#             # self.send(data.decode())
#
#     def send(self, msg: str):
#         self.sock.send(msg.encode())
#
#     def stop(self):
#         self.sock.close()
#         self.event.set()
#
#
# def main():
#     cc1 = ChatUDPClient()
#     cc2 = ChatUDPClient()
#     cc1.start()
#     cc2.start()
#     print(cc1.sock)
#     print(cc2.sock)
#     while True:
#         cmd = input('>>>')
#         if cmd.strip() == 'quit':
#             cc1.stop()
#             cc2.stop()
#             break
#         cc1.send(cmd)
#         cc2.send(cmd)
#
#
# if __name__ == '__main__':
#     main()


# import socket
# import threading
# import logging
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
#
# class ChatUDPClient:
#     def __init__(self, ip='127.0.0.1', port=9999, interval=5):
#         self.sock = socket.socket(socket.SOCK_DGRAM)
#         self.address = ip, port
#         self.event = threading.Event()
#         self.interval = interval
#
#     def start(self):
#         self.sock.connect(self.address)  # 占用本地地址和端口，设置远端地址和端口
#         threading.Thread(target=self.receive, name='receive').start()
#         threading.Thread(target=self.send_hb, name='send_hb', daemon=True).start()
#
#     def receive(self):
#         while not self.event.is_set():
#             data, raddr = self.sock.recvfrom(1024)
#             msg = '{} from {}:{}'.format(data.decode(), *raddr)
#             logging.info(msg)
#
#     def send_hb(self):  # 发送心跳信息
#         while not self.event.wait(self.interval):
#             self.send('^hb^')
#
#     def send(self, msg: str):
#         self.sock.sendto(msg.encode(), self.address)
#
#     def stop(self):
#         self.send('quit')
#         self.sock.close()
#         self.event.set()
#
#
# def main():
#     cc1 = ChatUDPClient()
#     cc2 = ChatUDPClient()
#     cc1.start()
#     cc2.start()
#     print(cc1.sock)
#     print(cc2.sock)
#     while True:
#         cmd = input('>>>>')
#         if cmd.strip() == 'quit':
#             cc1.stop()
#             cc2.stop()
#             break
#         cc1.send(cmd)
#         cc2.send(cmd)
#
#
# if __name__ == '__main__':
#     main()


# import socketserver
# import threading
#
#
# # MyTCPHandler继承自BaseRequestHandler，BaseRequestHandlerClass
# # 在BaseServer中实例化传三个参数，是因为BaseRequestHandler
# # init定义了三个参数
# class EchoHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         print(1, self.request)
#         print(2, self.client_address)
#         print(3, self.server)
#         print(4, self.__dict__)
#         print(5, self.server.__dict__)
#         print(6, threading.enumerate())
#         print(7, threading.current_thread())
#         for i in range(3):
#             data = self.request.recv(1024).strip()
#             self.request.send(data)
#             print(data)
#
#
# HOST, PORT = "127.0.0.1", 9999
# # 同步
# echoserver = socketserver.TCPServer((HOST, PORT), EchoHandler)
# # 异步
# # echoserver = socketserver.ThreadingTCPServer((HOST, PORT), EchoHandler)
# echoserver.serve_forever()
# print('------')
# echoserver.server_close()
# print('========')


# import threading
# import socketserver
#
#
# class MyHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         # super().handle()  # 可以不调用，父类handle什么都没有做
#         print('-'*30)
#         print(self.server)  # 服务
#         print(self.request, '====')  # 服务端负责客户端连接请求的socket对象
#         print(self.client_address)  # 客户端地址
#         print(self.__dict__)
#         print(self.server.__dict__)  # 能看到负责accept的socket
#
#         print(threading.enumerate())
#         print(threading.current_thread())
#         print('='*30)
#
#
# addr = ('127.0.0.1', 9999)
# server = socketserver.ThreadingTCPServer(addr, MyHandler)
# server.serve_forever()


# from socketserver import ThreadingTCPServer, BaseRequestHandler
# import threading
# import sys
#
#
# class EchoHandler(BaseRequestHandler):
#     clients = {}
#
#     def setup(self):
#         super().setup()
#         self.event = threading.Event()  # 初始工作
#         self.clients[self.client_address] = self.request
#
#     def finish(self):
#         super().finish()
#         self.clients.pop(self.client_address)
#         self.event.set()
#
#     def handle(self):
#         super().handle()
#         while not self.event.is_set():
#             data = self.request.recv(1024).decode()
#             if data == 'quit' or data == '':
#                 break
#             msg = '{} {}'.format(self.client_address, data).encode()
#             for s in self.clients.values():
#                 s.send(msg)
#         print('End')
#
#
# addr = ('127.0.0.1', 9999)
# server = ThreadingTCPServer(addr, EchoHandler)
# print(server.handle_request())
# print('----')
# server_thread = threading.Thread(target=server.serve_forever, name='EchoServer', daemon=True)
# server_thread.start()
#
# try:
#     while True:
#         cmd = input('>>>')
#         if cmd.strip() == 'quit':
#             server.shutdown()
#             break
#         print(threading.enumerate())
# except EXception as e:
#     print(e)
# except KeyboardInterrupt:
#     pass
# finally:
#     print('Exit')
#     sys.exit(0)


import socketserver
import threading
import sys
import logging

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatHandler(socketserver.BaseRequestHandler):
    clients = {}

    def setup(self):
        super().setup()
        self.event = threading.Event()
        self.clients[self.client_address] = self.request

    def finish(self):  # BaseRequestHandler有上下文保证会执行finish
        super().finish()
        self.clients.pop(self.client_address)
        self.event.set()

    def handle(self):
        while not self.event.is_set():
            data = self.request.recv(1024)
            if data.strip() == b'quit' or data == b'':
                break
            msg = '{} {}'.format(self.client_address, data).encode()
            logging.info(msg)
            for c in self.clients.values():
                c.send(msg)


addr = ('127.0.0.1', 9999)
server = socketserver.ThreadingTCPServer(addr, ChatHandler)
# server.serve_forever()  # 阻塞
server_thread = threading.Thread(target=server.serve_forever, name='ChatServer', daemon=True)
server_thread.start()

try:
    while True:
        cmd = input('>>>')
        if cmd == 'quit':
            server.server_close()
            break
        print(threading.enumerate())
except Exception as e:
    print(e)
except KeyboardInterrupt:
    pass
finally:
    print('Exit')
    sys.exit(0)
















































