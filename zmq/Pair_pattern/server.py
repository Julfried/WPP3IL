import zmq
import time
port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)
while True:
    # msg = socket.recv()
    msg = b"Server message to client"
    print(msg)
    socket.send(msg)
    time.sleep(2)