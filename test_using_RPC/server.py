from pizza_pb2_grpc import PizzaRPCServicer
import pizza_pb2
import grpc
from concurrent import futures


class MyPizzaServicer(PizzaRPCServicer):
    
    def __init__(self):
        self.__size = 0
    
    def SetFileSize(self, request, context):
        print("Coucou")
        # request is type pizza_pb2.Size
        self.__size = request.size
        print(f"My size is now {self.__size}")
        return pizza_pb2.Empty()
    
    @property
    def size(self):
        return self.__size
    
    
class Server:
    
    def __init__(self, port):
        self._servicer = MyPizzaServicer()
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self._server.add_insecure_port(f'[::]:{port}')
        self.start()
        
    def start(self):
        self._server.start()
        print("Server started")
        self._server.wait_for_termination()
        

if __name__ == "__main__":
    myserver = Server("32323")
    myserver.start()