import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('创建进程失败')
elif pid == 0:
    sleep(3)
    print('子进程退出',os.getpid())
    os._exit(2)
else:
    pid,status = os.waipidt(-1,os=WONHANG)
    print(pid,status)
    print(os.WEXITSTATUS(status)) #获取子进程退出状态
    while True:
        pass