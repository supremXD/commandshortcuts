import os, socket



def menu():
    print("")
    print("\033[92mWelcome to autoserver, please select an option:\033[92m\033[97m\033[97m")
    print("")
    print("1---> Start python3 server")
    print("2---> Download from a server")
    print("3---> Exit")
    option = input("Select an option---> ")
    if option == "1":
        print("")
        ip()
        print("")
        print("\033[93mStarting server. Press Ctrl+C to stop.\033[93m\033[97m\033[97m")
        print("")
        os.system("python3 -m http.server 8080")
        exit()
    if option == "2":
        print("")
        ip_from_download = input("Write the local IP from wich the download (e.g:192.168.1.125)---> ")
        port_to_download = input("Write the port of the local IP from wich the download---> ")
        file_to_download = input("Write the name of the file to download---> ")
        directory_to_download = input("Write the directory of the file to be downloaded (. to here)--->")
        os.system("wget http://"+ip_from_download+":"+port_to_download+"/"+file_to_download+" -P "+directory_to_download+"")
        print("\033[92mDone!\033[92m")
        exit()
    if option == "3":
        exit()


def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_local = s.getsockname()[0]
    s.close()
    print(f"Your local ip is: {ip_local}, access by: \033[92mhttp://{ip_local}:8080\033[92m")



menu()