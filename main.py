import socket, threading

conn = ""

def clean():
    print("\n" * 100)

class threads (threading.Thread):
    cliser = ""
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        cliser = threadID
    def run(self):
        while True:
            DATA = conn.recv(4096)
            if DATA.decode() == "::exit": exit()
            print(">>> " + DATA.decode())

def server():
    global conn
    HOST = ""
    PORT = int(input("PORT >>> "))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(10)
        print("Waiting for connection...")
        conn, addr = server_socket.accept()
        print("Connected...\nWaiting for DATA...")
        with conn:
            clean()
            while True :
                thread1 = threads(1, "Thread-1", 1)
                thread1.start()
                sDATA = input("")
                if sDATA == "::exit": exit()
                conn.sendall(str.encode(sDATA))

def client():
    global conn
    HOST = input("HOST >>> ")
    PORT = int(input("PORT >>> "))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((HOST, PORT))
            conn = client_socket
            clean()
        except ConnectionRefusedError:
            print("Connection refused...")
            exit()
        while True:
            thread2 = threads(2, "Thread-2",  2)
            thread2.start()
            cDATA = input("")
            if cDATA == "::exit": exit
            client_socket.sendall(str.encode(cDATA))

if __name__ == "__main__":
    sor = int(input("1) USER1\n2) USER2\n____ >>> "))
    if sor == 1:
        client()
    elif sor == 2:
        server()
    else:
        print("Error")
