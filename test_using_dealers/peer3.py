
import zmq
import time

context = zmq.Context()

# Dealer socket for sending messages
dealer_socket = context.socket(zmq.DEALER)
dealer_socket.identity = b"Peer3"  # Set unique identity
connected = dealer_socket.connect("tcp://localhost:5555")  # Connect to Peer 2's router
print(f"Peer 3 connected: {connected} to peer 2")

connected = dealer_socket.connect("tcp://localhost:5557")  # Connect to Peer 2's router
print(f"Peer 3 connected: {connected} to peer 4")


dealer_socket.bind("tcp://*:5556")  # Bind to port for others to connect

poller = zmq.Poller()
poller.register(dealer_socket, zmq.POLLIN)

#dealer_socket.send_multipart([dealer_socket.identity,"None".encode(), "hello from client 1".encode()])
for i in range(2):
    dealer_socket.send_multipart(["connexion".encode()])

while True:
    events = dict(poller.poll(timeout=0))  # Wait for 1 second (adjustable)
    
    if events:
        for socket, event in events.items():
            if socket == dealer_socket and event == zmq.POLLIN: 
                message = dealer_socket.recv_multipart()
                
                if len(message) == 1:
                    continue
                if (message[1].decode() == "None"):
                    for i in range(2):
                        dealer_socket.send_multipart([dealer_socket.identity,message[0],message[2]])
                    
                else:
                    if (message[1].decode() != dealer_socket.identity.decode()):
                        print(f"Received {message[2].decode()} from {message[0].decode}")
                        
                        for i in range(2):
                            dealer_socket.send_multipart([dealer_socket.identity,message[0],message[2]])
"""
import zmq
import time

context = zmq.Context()

# Dealer socket for sending messages
dealer_socket = context.socket(zmq.DEALER)
dealer_socket.identity = b"Peer3"  # Set unique identity
connected = dealer_socket.connect("tcp://localhost:5555")  # Connect to Peer 2's router
print(f"Peer 3 connected: {connected} to peer 2")

connected = dealer_socket.connect("tcp://localhost:5554")  # Connect to Peer 2's router
print(f"Peer 3 connected: {connected} to peer 1")


dealer_socket.bind("tcp://*:5556")  # Bind to port for others to connect


poller = zmq.Poller()
poller.register(dealer_socket, zmq.POLLIN)

#dealer_socket.send_multipart([dealer_socket.identity,"None".encode(), "hello from client 1".encode()])

dealer_socket.send_multipart(["connexion".encode()])

while True:
    events = dict(poller.poll(timeout=0))  # Wait for 1 second (adjustable)

    if events:
        for socket, event in events.items():
            if socket == dealer_socket and event == zmq.POLLIN: 
                message = dealer_socket.recv_multipart()
                if len(message) == 1:
                    continue
                if (message[1].decode() == "None"):
                    dealer_socket.send_multipart([dealer_socket.identity,message[0],message[2]])
                    print(f"received from source {message}")
                else:
                    if (message[1].decode() != dealer_socket.identity.decode()):
                        print(f"Received {message[2].decode()} from {message[0].decode}")
                        
                        dealer_socket.send_multipart([dealer_socket.identity,message[0],message[2]])"""