# import logging
#
# FORMAT = '%(asctime)-15s\tThread info: %(thread)d %(threadName)s %(message)s'
# logging.basicConfig(format=FORMAT)
#
# logging.info('I am {}'.format(20))
# logging.warning('I am {}'.format(20))


# import logging
#
# FORMAT = '%(asctime)-15s\tThread info: %(thread)d %(threadName)s %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# logging.info('I am {}'.format(20))
# logging.info('I am %d %s', 20, 'years old.')


# import logging
#
# FORMAT = '%(asctime)s Thread info: %(thread)s %(threadName)s' \
#          ' %(school)s %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.WARNING,
#                     datefmt='%Y%m%d---%H:%M:%S')
#
# d = {'school': 'xxx'}
# logging.warning('I am {}'.format(20), extra=d)
# logging.error('I am %d %s', 20, 'years old', extra=d)


# import logging
#
# logging.basicConfig(format='%(asctime)s %(message)s',
#                     filename='C:/Users/Zoes/Videos/EDU_Python/test.log')
# for _ in range(5):
#     logging.warning('this event was logged')


# import logging
#
# # log = logging.getLogger()
# log = logging.getLogger('s')
# print(log.name, logging.root.name)
# print(id(logging.root))
# print(id(log))


# import logging
#
# root = logging.getLogger()
# print(root.name, type(root), root.parent, id(root))
#
# logger = logging.getLogger(__name__)
# print(logger.name, type(logger), id(logger.parent), id(logger))
#
# loggerchild = logging.getLogger(__name__ + '.child')
# print(loggerchild.name, type(loggerchild), id(loggerchild.parent), id(loggerchild))
#


# import logging
#
# FORMAT = '%(asctime)s-15s\tThread info: %(thread)d %(threadName)s %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# logger = logging.getLogger(__name__)
# print(logger.name, type(logger))
# print(logger.getEffectiveLevel())
#
# logger.info('hello1')
# logger.setLevel(28)
#
# print(logger.getEffectiveLevel())
# logger.info('hello2')
# logger.warning('hello3 warning')
#
# root = logging.getLogger()
# root.info('hello4 info root')

# import logging
#
# FORMAT = '%(asctime)s %(name)s %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# logger = logging.getLogger('test')
# print(logger.name, type(logger))
#
# logger.info('line1')
#
# handler = logging.FileHandler('C:/Users/Zoes/Videos/EDU_Python/test1.log')
# logger.addHandler(handler)
# handler.setLevel(50)
#
# logger.info('line2')


# import logging
#
# FORMAT = '%(asctime)s %(name)s %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)
#
# root = logging.getLogger()
# log1 = logging.getLogger('s')
# log1.setLevel(logging.ERROR)
#
# log2 = logging.getLogger('s.s1')
# log2.warning('log warning')


import logging

logging.basicConfig(format='%(name)s %(asctime)s %(message)s',
                    level=logging.INFO)

root = logging.getLogger()
root.setLevel(logging.ERROR)
print('root', root.handlers)
h0 = logging.StreamHandler()
h0.setLevel(logging.WARNING)
root.addHandler(h0)
print('root', root.handlers)
for h in root.handlers:
    print('root handler = {}, formatter = {}'.format(h, h.formatter))

log1 = logging.getLogger('s')
log1.setLevel(logging.ERROR)
h1 = logging.FileHandler('C:/Users/Zoes/Videos/EDU_Python/test2.log')
h1.setLevel(logging.WARNING)
log1.addHandler(h1)
print('log1', log1.handlers)























































































