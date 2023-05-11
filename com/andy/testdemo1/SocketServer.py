from socket import *

def tcp_server():
    socketserver = socket(AF_INET,SOCK_STREAM)
    addr = ("192.168.15.106",40222)

    socketserver.bind(addr)
    socketserver.listen(5)
    client,add = socketserver.accept()
    client.send("你好，这里是服务器端".encode("utf-8"))
    recive = client.recv(1024)
    print(recive.decode("utf-8"))

def udp_server():
    socketserver = socket(AF_INET, SOCK_DGRAM)
    addr = ("192.168.15.106", 40222)
    socketserver.bind(addr)
    recive = socketserver.recvfrom(1024)
    print(recive[0].decode("utf-8"))
    socketserver.sendto("你好，这里是服务器端".encode("utf-8"),recive[1])
    socketserver.close()

if __name__ == '__main__':
    udp_server()