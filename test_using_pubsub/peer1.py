import zmq
import time
context = zmq.Context()

# PGM multicast address (replace with your desired multicast group)
pub_address = "tcp://*:5555"

publisher = context.socket(zmq.PUB)
publisher.bind(pub_address)
i = 0
while i < 10:
    message = f"Hello from Peer1 - {i}".encode()
    publisher.send(message)
    print("Published message:", message)
    # Simulate some workload
    time.sleep(0.1)
    i +=1