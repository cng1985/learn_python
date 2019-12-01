import socket
host = '127.0.0.1'
port = 6666
addr = (host, port)
tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(addr)
while True:
    msg = input('请输入：')
    if not msg:
        break
    tcpCliSock.send(msg.encode())
    data = tcpCliSock.recv(2048)
    if not data:
        break
    print(data.decode())
