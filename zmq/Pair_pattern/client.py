import zmq
import time
port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)
while True:
    # socket.send(b"client message to server1")
    msg = socket.recv()
    print(msg)
    time.sleep(1)