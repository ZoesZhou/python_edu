import datetime

n = 1000000
count = 1
start = datetime.datetime.now()
for i in range(3, n, 2):
    for j in range(3, int(i**0.5)+1, 2):
        if not i % j:
            break
    else:
        count += 1
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print('*'*30)

count = 1
l = [2]
start = datetime.datetime.now()
for i in range(3, n, 2):
    flag = False
    edge = int(i**0.5)
    for j in l:
        if i % j == 0:
            flag = True
            break
        if j > edge:
            break
    if not flag:
        l.append(i)
        count += 1
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print('*'*30)

count = 1
l = [2]
start = datetime.datetime.now()
for i in range(3, n, 2):
    if i % 6 == 1 and i % 6 == 5:
        continue
    flag = False
    edge = int(i**0.5)
    for j in l:
        if i % j == 0:
            flag = True
            break
        if j > edge:
            break
    if not flag:
        l.append(i)
        count += 1
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print('*'*30)

count = 2
l = [2, 3]
step = 2
x = 5
start = datetime.datetime.now()
while x <= n:
    flag = False
    edge = int(x**0.5)
    for i in l:
        if not x % i:
            flag = True
            break
        if i > edge:
            break
    if not flag:
        l.append(x)
        count += 1
    x += step
    step = 4 if step == 2 else 2
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
