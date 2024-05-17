import zenoh, random, time
import threading
random.seed()


main_topic = "node3"

def read_temp():
    return random.randint(15, 30)

def listener(sample):
    print(f"Received from node1 {sample.kind} ('{sample.key_expr}': '{sample.payload.decode('utf-8')}')")
    
if __name__ == "__main__":
    session = zenoh.open()
    key = 'node1'
    pub = session.declare_publisher(key)

    while True:
        t = read_temp()
        buf = f"{t}"
        print(f"Putting Data ('{key}': '{buf}')...")
        pub.put(buf)
        time.sleep(1)