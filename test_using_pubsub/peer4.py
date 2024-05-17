import zmq
import time
import threading
import asyncio

MESSAGE = None

def publisher(response):
    context2 = zmq.Context()

    pub_address = "tcp://*:5457"
    publisher = context2.socket(zmq.PUB)
    publisher.bind(pub_address)
    
    publisher.send("connexion".encode())
    message = f"{response}".encode()
    time.sleep(0.001)
    publisher.send(message)
    print(f"Putting Data ('{message}')...")
    


def subscriber():
    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    subscriber.setsockopt(zmq.SUBSCRIBE, b"")
    subscriber.connect("tcp://localhost:5555")

    while True:
        message = subscriber.recv()
        print(message)
        time.sleep(0.001)
        thread_pub = threading.Thread(target=publisher, args=(str(f"{message.decode()}"),))
        thread_pub.start()
        thread_pub.join()
        print("Received:", message.decode())


if __name__ == "__main__":
    subscriber()