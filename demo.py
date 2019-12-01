import data.datademo as demo
import webbrowser
import socket

demo.showMessage()

sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen(5)

conn,address = sk.accept()
sk.sendall(bytes("Hello world",encoding="utf-8"))
