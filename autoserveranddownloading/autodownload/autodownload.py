import os, socket



def download():
    print("")
    ip_from_download = input("Write the local IP from wich the download (e.g:192.168.1.125)---> ")
    port_to_download = input("Write the port of the local IP from wich the download---> ")
    file_to_download = input("Write the name of the file to download---> ")
    directory_to_download = input("Write the directory of the file to be downloaded (. to here)--->")
    os.system("wget http://"+ip_from_download+":"+port_to_download+"/"+file_to_download+" -P "+directory_to_download+"")
    print("\033[92mDone!\033[92m")
    exit()



download()