import threading
from time import sleep,ctime
def run():
    for i in range(5):
        print("跑步")
        sleep(1)

def sing():
    for i in range(5):
        print("唱歌")
        sleep(1)

def main():
    print("开始--%s"%ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()
    while True:
        #查看当前线程数量
        length = len(threading.enumerate())
        print("当前线程数%d"%length)
        if length <= 1:
            print("结束--%s"%ctime())
            break
        sleep(0.5)
if __name__ == "__main__":
    main()