import zenoh, random, time
import messages
import pickle
msg = messages.Add(1,2,1,2)

random.seed()
with open("pickled_data.pkl", "wb") as f:
    pkl = pickle.dump(msg,f)
    print(pkl)
def read_temp():
    return random.randint(15, 30)

if __name__ == "__main__":
    session = zenoh.open()
    key = 'myhome/kitchen/temp'
    pub = session.declare_publisher(key)
    i = 0
    while i < 10:
        i+=1
        t = read_temp()
        buf = f"{t}"
        print(f"Putting Data ('{key}': '{buf}')...")
        pub.put(msg.to_json())
        #time.sleep(1)