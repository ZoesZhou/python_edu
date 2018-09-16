import argparse
import stat
import datetime
from pathlib import Path

parser = argparse.ArgumentParser(
    prog='ls',
    description='List information about the FILEs',
    add_help=False
)  # 获取一个参数解析器
parser.add_argument('path', nargs='?', default='.',
                    help='file path')  # 位置参数
parser.add_argument('-l', dest='list', action='store_true',
                    help='use a long listing format')
parser.add_argument('-a', '--all', action='store_true',
                    help='do not ignore entries starting with .')
parser.add_argument('-h', '--human-readable', dest='human', action='store_true',
                    help='with -l, print sizes in human readable format (e.g., 1K 234M 2G')

# args = parser.parse_args()  # 分析参数，同时传入可迭代的参数


# parse_args(args=None, namespace=None) args参数列表，一个可迭代对象。
# 内部会把可迭代对象装换成list。如果为None则使用命令行传入参数，非None
# 则使用args参数的可迭代对象

# print('--------------------------')
# parser.print_help()  # 打印帮助

# print(args)  # 打印名词空间中收集的参数
# print(args.all, args.list, args.path)  # Namespace(path='/etc')里面的path
# 参数存储在了一个Namespace对象内的属性上，可以通过Namespace对象属性来
# 访问，例如args.path
# print(1, args.path, type(args.path))
# 以上程序是通过模仿Linux通过敲命令来获取目录路径


def iter_dir(p1: str, all=False, detail=False, human=False):
    # 以下程序得到目录路径，迭代显示里面的文件的详细信息
    def _get_file_type(p: Path):
        if p.is_dir():
            return 'd'
        elif p.is_block_device():
            return 'b'
        elif p.is_char_device():
            return 'c'
        elif p.is_fifo():
            return 'p'
        elif p.is_socket():
            return 's'
        elif p.is_symlink():
            return 'l'
        else:
            return '-'

    # st.st_mode的值是十进制，转成八进制（'0o40777'）只留后三位，&0o777，=0b111111111
    mode_list = ['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']

    # def _get_mode(mode: int):  # 这种做法有风险，当bin(mode)不够9位时，
    #     mode = mode & 0o777  # 要把 0b 去掉，在前面补0凑够9位
    #     print(mode)
    #     print(mode, bin(mode))
    #     mode_str = ''
    #     for i, c in enumerate(bin(mode)[-9:]):
    #         if c == 1:
    #             mode_str += mode_list[i]
    #         else:
    #             mode_str += '-'
    #     return mode_str

    def _get_mode(mode: int):
        mode = mode & 0o777
        mode_str = ''
        for i in range(8, -1, -1):
            m = mode >> i & 1
            if m:
                mode_str += mode_list[8-i]
            else:
                mode_str += '-'
        return mode_str

    def _get_size(size: int):
        index = 0
        units = ' KMGT'
        while size >= 1000:
            index += 1
            size = size // 1000
        return '{}{}'.format(size, units[index])

    def listdir(p1: str, all=False, detail=False, human=False):
        path = Path(p1)
        for x in path.iterdir():
            if not all and x.name.startswith('.'):
                continue
            if not detail:  # 打印详细信息
                st = path.stat()
                # print(st)
                t = _get_file_type(path)
                # mode = _get_mode(st.st_mode)
                # mode = stat.filemode(st.st_mode)  # 使用内建库
                a_time = datetime.datetime.fromtimestamp(st.st_atime).strftime("%Y/%m/%d %H:%M:%S")
                human = str(st.st_size) if not human else _get_size(st.st_size)
                yield (t+_get_mode(st.st_mode), st.st_nlink, st.st_uid, st.st_gid, human, a_time, x.name)
            else:
                yield (x.name,)
    yield from sorted(listdir(p1, all, detail, human), key=lambda x: x[-1])


if __name__ == '__main__':
    args = parser.parse_args()  # 分析参数，同时传入可迭代的参数
    file_name = iter_dir(args.path, args.all, args.list, args.human)
    print(list(file_name))