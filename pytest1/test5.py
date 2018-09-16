# from functools import _make_key
#
# key = _make_key((1, 3, 5), {'x': 6, 'y': 9}, False)
# print(key)
# print(hash(key))


# def copy_properties(original):
#     def _copy(new):
#         new.__name__ = original.__name__
#         new.__doc__ = original.__doc__
#         return new
#     return _copy
#
#
# def logger(fn):
#     @copy_properties(fn)
#     def _logger(*args):
#         """_logger function
#
#         :param args:
#         :return:
#         """
#         print(args)
#         return fn(*args)
#     return _logger
#
#
# @logger
# def add(x: int, y: int):
#     """add function
#
#     :param x: int
#     :param y: int
#     :return:
#     """
#     return x + y
#
#
# print(add(3, 4))
# print(add.__name__, add.__doc__)


alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64encode(src: str):
    ret = bytearray()
    if isinstance(src, str):
        _src = src.encode()
    else:
        return

    length = len(_src)
    r = 0
    for offset in range(0, length, 3):
        val = _src[offset:offset+3]

        if offset + 3 > length:
            r = 3 - len(val)
            val += b'\x00' * r

        b = int.from_bytes(val, 'big')

        for i in range(18, -1, -6):
            if i == 18:
                index = b >> i
            else:
                index = b >> i & 0x3F   #0x3F  # 0b111111
            ret.append(alphabet[index])

    if r:
        ret[-r:] = b'=' * r
    return bytes(ret)


print(base64encode('a'))


# alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
#
#
# def base64encode(src: str):
#     if isinstance(src, str):
#         _src = src
#     else:
#         _src = src
#
#     length = len(_src)
#     for i in
