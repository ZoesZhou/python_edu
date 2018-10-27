print(__name__)
print('---------------')


class A:
    def show_moudle(self):
        print(self.__class__.__name__)


if __name__ == '__main__':
    a = A()  # 程序运行方式__name__ = __main__
    a.show_moudle()
else:
    print('add')  # 以模块导入的方式运行时，__name__ = 模块名
    