from socket import *
# AF_INET ipv4
# SOCK_STREAM TCP 协议
# SOCK_DGRAM UDP协议
def tcp_client():
    socketClient = socket(AF_INET,SOCK_STREAM)
    addr = ("192.168.15.106",40222)
    socketClient.connect(addr)
    recive = socketClient.recv(1024)
    print(recive.decode("utf-8"))
    socketClient.send("这里是客户端".encode("utf-8"))

def udp_client():
    socketClient = socket(AF_INET, SOCK_DGRAM)
    addr = ("192.168.15.106", 40222)
    socketClient.sendto("Hello".encode("utf-8"),addr)
    recive = socketClient.recvfrom(1024)
    print(recive[0].decode("utf-8"))
    socketClient.close()

if __name__ == '__main__':
    udp_client()

