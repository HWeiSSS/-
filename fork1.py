import os
from time import sleep

def f1():
    sleep(3)
    print('第一件事')

def f2():
    sleep(4)
    print('第二件事')

pid = os.fork()

if pid < 0:
    print('创建进程失败')
elif pid == 0:
    p = fork()
    if p == 0:
        f2()
    else:
        os._exit(0)
else:
    os.wait()
    f1()  