import zenoh, time
import pickle
from io import BytesIO
from messages import Message
import json

def listener(sample):
    """print(sample.payload.decode('utf-8'))
    with BytesIO(sample.payload) as f:

        msg = pickle.load(f)"""
    
    
    msg = Message.from_json(sample.payload.decode('utf-8'))
    print(type(msg))
    print(f"Received {sample.kind} ('{sample.key_expr}': '{msg.id_sender}')")

if __name__ == "__main__":
    session = zenoh.open()
    sub = session.declare_subscriber('myhome/kitchen/temp', listener)
    #time.sleep(60)