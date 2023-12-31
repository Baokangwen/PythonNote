#模拟这种状态   两个线程 t1 和 t2 都要对全局变量 g_num进行十次累加  最终的结果两个线程都应该是10
#有可能出现什么情况 t1 g_num=0 t1 睡眠状态  t2开始运行 g_num=0
#2.t2 加一 修改了全局的g_num = 1
#3.t2 sleeping t1 g_num=1
#4.这样是不是导致了一种情况，都加了1，本来是2，但是结果仍然是1

import threading
import time
g_num=0

def work1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("work1,g_num is %d" %g_num)

def work2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("work2,g_num is %d" %g_num)
print("没有线程之前 g_num is %d" %g_num)

t1 = threading.Thread(target=work1,args=(1000000,))
t1.start()
#延时保证t1线程先把事情做完

# time.sleep(1)

t2 = threading.Thread(target=work2,args=(1000000,))
t2.start()
while len(threading.enumerate())!=1:    #线程数量不等于1
    time.sleep(1)
print("最终结果是%d"%g_num)

#如果多个线程对同一个全局变量操作会出现资源竞争问题，导致数据不正确，线程不安全的问题
#同步 你的任务执行完我再做
#系统调用t1 获取到g_num的值是0，此时我们上锁不允许其他线程操作
#2,t1对他进行加1
#t1解锁，此时g_num=1其他线程就可以使用g_num 此时的g_num不是0而是1
#其他的线程在对这个数据操作的时候都要上锁，处理完解锁，上锁的过程中就不允许其他的线程访问变量