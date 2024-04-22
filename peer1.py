import zmq
import time

context = zmq.Context()

# Dealer socket for sending messages
dealer_socket = context.socket(zmq.DEALER)
dealer_socket.identity = b"Peer1"  # Set unique identity

connected = dealer_socket.connect("tcp://localhost:5555")  # Connect to Peer 2's router
print(f"Peer 1 connected: {connected} to peer 2")

connected = dealer_socket.connect("tcp://localhost:5557")  # Connect to Peer 2's router
print(f"Peer 1 connected: {connected} to peer 4")

connected = dealer_socket.connect("tcp://localhost:5558")  # Connect to Peer 2's router
print(f"Peer 1 connected: {connected} to peer 5")

connected = dealer_socket.connect("tcp://localhost:5559")  # Connect to Peer 2's router
print(f"Peer 1 connected: {connected} to peer 6")

dealer_socket.bind("tcp://*:5554")  # Bind to port for others to connect


"""
for i in range(4):
    v
    m = dealer_socket.recv_multipart()
    print(m)
"""




poller = zmq.Poller()
poller.register(dealer_socket, zmq.POLLIN)


for i in range(4):
    dealer_socket.send_multipart([dealer_socket.identity,"None".encode(), "voila".encode()])

while True:
    events = dict(poller.poll(timeout=0))  # Wait for 1 second (adjustable)

    if events:
        for socket, event in events.items():
            if socket == dealer_socket and event == zmq.POLLIN: 
            
            
                message = dealer_socket.recv_multipart()
                
                if len(message) == 1:
                    continue

                
                if (message[1].decode() != dealer_socket.identity.decode()):
                    print(f"Received {message}")
        
        #dealer_socket.send_multipart([message[0],"hello from client 1".encode()])

"""import zmq
import time

context = zmq.Context()

# Dealer socket for sending messages
dealer_socket = context.socket(zmq.DEALER)
dealer_socket.identity = b"Peer1"  # Set unique identity

connected = dealer_socket.connect("tcp://localhost:5555")  # Connect to Peer 2's router
print(f"Peer 1 connected: {connected} to peer 2")

connected = dealer_socket.connect("tcp://localhost:5556")  # Connect to Peer 2's router
print(f"Peer 1 connected: {connected} to peer 3")

dealer_socket.bind("tcp://*:5554")  # Bind to port for others to connect



for i in range(4):
    v
    m = dealer_socket.recv_multipart()
    print(m)

for i in range(2):
    dealer_socket.send_multipart([dealer_socket.identity,"None".encode(), "voila".encode()])

while True:

    message = dealer_socket.recv_multipart()
    
    if len(message) == 1:
        continue

    if (message[1].decode() != dealer_socket.identity.decode()):
        print(f"Received {message}")
        
        #dealer_socket.send_multipart([message[0],"hello from client 1".encode()])"""