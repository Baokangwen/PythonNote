import time
# 没有使用多任务的编程
def run():
    for i in range(5):
        print("跑步")
        time.sleep(1)

def sing():
    for i in range(5):
        print("唱歌")
        time.sleep(1)

def main():
    run()
    sing()

if __name__ == "__main__":
    main()