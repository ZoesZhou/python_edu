
# s = '112.64.118.97 - - [06/Apr/2017:19:13:59 +0800] "GET /favicon.ico HTTP/1.1" 200 4101 "-" "Dalvik/2.1.0' \
#         '(Linux; U; Android 5.1.1; SM-G9250 Build/LMY47X)"'


# def make_str(s: str, chars=set("""[]"'""")):
#     result = []
#     start = 0
#     length = len(s)
#     for i, c in enumerate(s):  # ..a
#         if c in chars:
#             if i == start:
#                 start += 1
#                 continue
#             result.append(s[start:i])
#             start = i + 1
#     else:
#         if start < length:
#             result.append(s[start:])
#     print(result)
#
#
# make_str(s)
import datetime
import re


def make_key(line:str, chars=set(""" []"'""")):
    start = 0
    flag = False
    for i, c in enumerate(line):
        if c in chars:
            if c == '[':  # 开始，直到右括号
                flag = True
                start = i + 1  # 跳过[
            elif c == ']':
                flag = False  # 结束
            elif c == '"':
                flag = not flag
                if flag:
                    start = i + 1
            if flag:
                continue
            if start == i:
                start = i + 1
            yield line[start:i]
            start = i + 1
    else:
        if start < len(line):
            yield line[start:]


line = '123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] "GET /o2o/media.html?menu=3 HTTP/1.1" 200 8642 "-" ' \
       '"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"'

names = ('remote', '', '', 'datetime', '', 'request', '', 'status', 'size', '', '', 'useargent')
# do_no_thing = lambda x: x  # 就不用判断ops里是不是函数了
ops = (None, None, None,
       lambda dstr: datetime.datetime.strptime(dstr, '%d/%b/%Y:%H:%M:%S %z'),
       None, lambda request: dict(zip(['method', 'url', 'protocol'], request.split())), None, int, int, None, None, None)

pattern = '([\d.]{7,15}) - - \[([^\[\]]*)\] "([\w]+) (.+) ([\w/\d.]+)" ([\d]+) ([\d]+) \S+ "([^"]*)"'
regex = re.compile(pattern)
matcher = regex.match(line)
if matcher:
    print(matcher)
    print(line[matcher.start():matcher.end()])
    print(1, matcher.group())
    print(2, matcher.groups())


def extract(line:str):
    return dict(
        map(lambda triple: (triple[0], triple[1](triple[2]) if triple[1] else triple[2]),
            zip(names, ops, make_key(line))
            )
    )


print(extract(line))
