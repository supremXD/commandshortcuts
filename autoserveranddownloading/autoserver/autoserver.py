import os, socket



def server():
    print("")
    ip()
    print("")
    print("\033[93mStarting server. Press Ctrl+C to stop.\033[93m\033[97m\033[97m")
    print("")
    os.system("python3 -m http.server 8080")
    exit()


def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_local = s.getsockname()[0]
    s.close()
    print(f"Your local ip is: {ip_local}, access by: \033[92mhttp://{ip_local}:8080\033[92m")



server()