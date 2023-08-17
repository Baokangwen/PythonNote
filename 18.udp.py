#python中做udp通信，我们采用socket
import socket

def main():
    #创建udp的套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #从键盘获取数据
    while True:
        send_data = input("输入数据:")
        #使用udp发送数据
        if send_data == "exit":
            break
        udp_socket.sendto(send_data.encode("gbk"),("192.168.1.100",8080))

    udp_socket.close()
if __name__ == '__main__':
    main()
