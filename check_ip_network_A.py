from threading import Thread
from multiprocessing.pool import ThreadPool as Pool
import queue
import time
import subprocess

IP_FIX = "10."
POOL_SIZE = 1
file = open("result_class_A.txt","w+")
q = queue.Queue()

def pingTask(addr):
    try:
        res = subprocess.check_output(["ping ", "-n", " 1", addr])
        if "unreachable" in str(res) or "timed out" in str(res):
            pass
        else:
            file.write(addr+"\n")
    except subprocess.CalledProcessError:
        pass
  
def ThreadPing(addr):
    try:
        T = Thread(target = lambda q,addr: q.put(pingTask(addr)), args=(q,addr))
        T.start()
        T.join()
        q.get()
    except expression as identifier:
        pass
    
pool = Pool(POOL_SIZE)
for net in range(1,255):
    for subnet in range(1,255):
        for host in range(1,255):
            addr = IP_FIX+str(net)+"."+str(subnet)+"."+str(host)
            pool.apply_async(ThreadPing, (addr,))

pool.close()
pool.join()