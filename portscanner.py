import socket
import threading
import time
from queue import Queue

print_lock = threading.Lock()


server = '0'
server = input('Insert an IP or website you want to scan!\nTo scan your local IP input "my IP"\n')

if server == "my ip" or server == "my IP":
    server = socket.gethostbyname(socket.gethostname())

server_ip = socket.gethostbyname(server)

print(server_ip)


def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((server_ip,port))
        with print_lock:
            print('Port ',port,"is open!")
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        pscan(worker)
        q.task_done()

q = Queue()

for x in range(777):
    t = threading.Thread(target=threader)
    t.deamon = True
    t.start()
for worker in range(1,10000):
    q.put(worker)

q.join

