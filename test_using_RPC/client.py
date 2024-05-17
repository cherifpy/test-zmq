from pizza_pb2_grpc import PizzaRPCServicer, PizzaRPCStub,PizzaRPC
import pizza_pb2
import grpc

class Client:
    
    def __init__(self):
        pass
    
    def setSizeOfServer(address, port, size):
        with grpc.insecure_channel(f'{address}:{port}') as channel:
            stub = PizzaRPCStub(channel)
            print("Coucou")
            ss = pizza_pb2.Size(size=size)
            print(stub)
            PizzaRPC.SetFileSize(ss)

if __name__ == "__main__":
    Client.setSizeOfServer("localhost","32323",15)    
