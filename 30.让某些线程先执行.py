import threading
import time
def run():
    for i in range(5):
        print("跑步")

def sing():
    for i in range(5):
        print("唱歌")

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=run)
    t1.start()
    time.sleep(1)
    print("第一个线程")
    t2.start()
    time.sleep(1)
    print("第二个线程")

if __name__ == "__main__":
    main()