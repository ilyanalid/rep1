import threading
import time
import matplotlib.pyplot as plt


def dot(v1, v2):
    global num
    res = v1*v2
    lock.acquire()
    num += res
    lock.release()

def thread(count,v1,v2):
    threads = [threading.Thread(target=dot, args = (v1[i],v2[i])) for i in range(0,count)]
    for th in threads:
        th.start()


num = 0
lock = threading.Lock()
v1 = [11111111111111,222222222222,3333333333333,4444444444]
v2 = [123123123123,345345345345,888888888888,1234567890]
start_time = time.time()
thread(len(v1),v1,v2)
finish = time.time() - start_time
print ('end\nscalar: {}.\ntime: {}.'.format(num, round(finish,10)))


def scalar(v1, v2):
    num = 0
    for i in range(len(v1)):
        res = v1[i]*v2[i]
        num += res
    return num

num_threads = [1,1,1,3,3,3]
time_th=[]
for k in range(3):
    start_time_th = time.time()
    scalar(v1,v2)
    finish_th = time.time() - start_time_th
    time_th.append(finish_th)
for k in range(3):
    start_time = time.time()
    thread(len(v1),v1,v2)
    finish = time.time() - start_time
    time_th.append(finish)

print(time_th)

plt.plot(time_th,num_threads)
plt.grid(True)
plt.show()
