import threading
import time


def showthreadinfo():
    print('currentthread = {}'.format(threading.current_thread()))
    print('mainthread = {}'.format(threading.main_thread()))
    print('active count = {}'.format(threading.active_count()))
    print(threading.enumerate())


def worker():
    count = 0
    showthreadinfo()
    while True:
        if count > 5:
            break
        time.sleep(1)
        count += 1
        print('I am working')


t = threading.Thread(target=worker, name='worker')
showthreadinfo()
# worker()
t.start()
print('=====end======')
print('=====end======')
print('=====end======')
print('=====end======')
print('=====end======')
print('=====end======')
