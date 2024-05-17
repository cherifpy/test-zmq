import zmq
import time
import threading
import asyncio


def publisher(response):
    context2 = zmq.Context()

    # PGM multicast address (replace with your desired multicast group)
    pub_address = "tcp://*:5455"
    publisher = context2.socket(zmq.PUB)
    publisher.bind(pub_address)
 
    publisher.send("connexion".encode())
    message = f"{response} forwarded from Peer2".encode()
    
    publisher.send(message)
    print(f"Putting Data ('{message}')...")
    


def subscriber():
    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    #ubscriber.setsockopt(zmq.SUBSCRIBE, b"")
    subscriber.connect("tcp://localhost:5555")
    
    poller = zmq.Poller()
    poller.register(subscriber, zmq.POLLIN)
    
    while True:
        message = subscriber.recv()
        print("Received:", message.decode())
        
        thread_pub = threading.Thread(target=publisher, args=(str(f"{message.decode()}"),))
        thread_pub.start()
        thread_pub.join()

        

if __name__ == "__main__":
    subscriber()