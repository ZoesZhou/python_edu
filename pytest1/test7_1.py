import argparse
from pathlib import Path
from datetime import datetime

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


def listdir(path, all=False, detail=False, human=False):
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
