import socket
def main():
    #创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定本地信息
    tcp_server_socket.bind(("",8888))
    #设置链接数
    tcp_server_socket.listen(128)
    #等待客户端链接
    new_client_socket,client_addr=tcp_server_socket.accept()
    print(client_addr)
    #接收客户端发送过来的数据
    rec_data = new_client_socket.recv(1024)
    print(rec_data)

    #回送数据给客户端
    new_client_socket.send("hello--ok--".encode("utf-8"))
    new_client_socket.close()
    tcp_server_socket.close()
if __name__ == '__main__':
    main()