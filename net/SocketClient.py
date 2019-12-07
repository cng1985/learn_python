import asyncore
import struct
import threading
a=[0x00, 0x00, 0x00, 0x2c, 0x63, 0x00, 0x00, 0x00,
    0x75, 0x4b, 0xef, 0x0f, 0x00, 0x03, 0x00, 0x00,
    0x01, 0x00, 0x00, 0x7f, 0x00, 0x01, 0x00, 0x00,
    0x88, 0x9f, 0xfa, 0xfd, 0x9f, 0x22, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x01]
     
     
class SocketClient(asyncore.dispatcher):
        def __init__(self, host, port,buffer=""):
            asyncore.dispatcher.__init__(self)
            self.create_socket()
            self.connect( (host, port) )
            self.buffer=buffer
        def handle_connect(self):
            print("handle_connect")
            pass
        def handle_close(self):
            print("handle_close")
            self.close()
        def handle_read(self):
            print("handle_read")
            print(self.recv(81920))
        def writable(self):
            print("writable")
            return (len(self.buffer) > 0)
        def handle_write(self):
            print("handle_write")
            sent = self.send(self.buffer)
            self.buffer = self.buffer[sent:]
     
    class SocketClientThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run(self):
            client = SocketClient("127.0.0.1", 6666)
            client.buffer = struct.pack("%dB" % (len(a)), *a)
            asyncore.loop()
     
     
    SocketClientThread().start()
