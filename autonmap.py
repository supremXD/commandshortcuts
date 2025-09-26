import os, sys, socket, ipaddress, time

banner = """

:'######:'##::::'##'########:'########:'########'##::::'##:
'##... ##:##:::: ##:##.... ##:##.... ##:##.....::###::'###:
 ##:::..::##:::: ##:##:::: ##:##:::: ##:##:::::::####'####:
. ######::##:::: ##:########::########::######:::## ### ##:
:..... ##:##:::: ##:##.....:::##.. ##:::##...::::##. #: ##:
'##::: ##:##:::: ##:##::::::::##::. ##::##:::::::##:.:: ##:
. ######:. #######::##::::::::##:::. ##:########:##:::: ##:
:......:::.......::..::::::::..:::::..:........:..:::::..::                                               
                                                                                                                                       
"""



def menu():
    os.system("clear")
    print(banner)
    print("")
    print("              |                    1-->> Scan full network")
    print("              |                    2-->> Scan IP")
    print("              |                    3-->> Macfinder")
    x = input("              ↳ ")
    if int(x) == 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
        except Exception:
            local_ip = None
        while not local_ip:
            personal_ip = input("Couldn't get your IP, type it --> ").strip()
            try:
                ipaddress.ip_address(personal_ip)
                local_ip = personal_ip  
            except ValueError:
                print("Invalid IP format. Must be a.b.c.d - Try again.")
        parts = local_ip.split('.')
        parts[-1] = '0'
        network = '.'.join(parts) + '/24'
        os.system("clear")
        print(banner)
        print("")
        print("              |                    1-->> Don't export output")
        print("              |                    2-->> Export in normal")
        print("              |                    3-->> Export in xml")
        print("              |                    4-->> Export in script kiddie")
        print("              |                    5-->> Export in grepable")
        print("              |                    6-->> Return")
        y = input("              ↳ ")
        print(f"Scanning your network ({network})")
        time.sleep(3)
        if int(y) == 1:
            os.system("clear")
            os.system(f"nmap {network} --min-rate 5000 -Pn -n --open")
            sys.exit(0)
        if int(y) == 2:
            os.system(f"nmap {network} --min-rate 5000 -Pn -n --open -oN output.txt")
            os.system("clear")
            print("Scan saved as output.txt")
            sys.exit(0)
        if int(y) == 3:
            os.system(f"nmap {network} --min-rate 5000 -Pn -n --open -oX output.txt")
            os.system("clear")
            print("Scan saved as output.txt")
            sys.exit(0)
        if int(y) == 4:
            os.system(f"nmap {network} --min-rate 5000 -Pn -n --open -oS output.txt")
            os.system("clear")
            print("Scan saved as output.txt")
            sys.exit(0)
        if int(y) == 5:
            os.system(f"nmap {network} --min-rate 5000 -Pn -n --open -oG output.txt")
            os.system("clear")
            print("Scan saved as output.txt")
            sys.exit(0)
        if int(y) == 6:
            menu()
    if int(x) == 2:
        print("")
        victim_ip= input("Place the ip to scan here -->> ")
        global v_ip
        v_ip = victim_ip.strip()
        parts = v_ip.split(".")
        if len(parts) != 4:
            print("Invalid IP format. Must be a.b.c.d")
            return
        else:
            attack()

    if int(x) == 3:
        print("")
        file = "macfinder.py"
        url = "https://raw.githubusercontent.com/supremXD/commandshortcuts/refs/heads/main/macfinder.py"
        os.system("clear")
        print(banner)
        print("")
        if not os.path.exists(file):
            os.system(f"wget {url} -O {file}")
        if os.path.exists(file):
            mac = input("MAC address -->> ")
            os.system(f"python3 {file}")


def attack():
    os.system("clear")
    print(banner)
    print("")
    print("              |                    1-->> Basic attack")
    print("              |                    2-->> All ports")
    print("              |                    3-->> All ports and versions")
    print("              |                    4-->> All ports and scripts")
    print("              |                    5-->> OS scan")
    print("              |                    6-->> Intense scan (all ports, versions, scripts, and OS scan)")
    print("              |                    7-->> Specific port")
    print("              |                    8-->> Return")
    z = input("              ↳ ")
    if int(z) == 1:
        print("")
        save_1 = input("Do you want to save the output file? (y/n) -->> ")
        if save_1 == "y":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -Pn -n --open -oN scan.txt")
            sys.exit(0)
        if save_1 == "n":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -Pn -n --open")
            sys.exit(0)
    if int(z) == 2:
        print("")
        save_2 = input("Do you want to save the output file? (y/n) -->> ")
        if save_2 == "y":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -p- -Pn -n --open -oN scan.txt")
            sys.exit(0)
        if save_2 == "n":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -p- -Pn -n --open")
            sys.exit(0)
    if int(z) == 3:
        print("")
        save_3 = input("Do you want to save the output file? (y/n) -->> ")
        if save_3 == "y":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -p- -sV -Pn -n --open -oN scan.txt")
            sys.exit(0)
        if save_3 == "n":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -p- -sV -Pn -n --open")
            sys.exit(0)
    if int(z) == 4:
        print("")
        save_4 = input("Do you want to save the output file? (y/n) -->> ")
        if save_4 == "y":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -p- -sC -Pn -n --open -oN scan.txt")
            sys.exit(0)
        if save_4 == "n":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -p- -sC -Pn -n --open")
            sys.exit(0)
    if int(z) == 5:
        print("")
        save_5 = input("Do you want to save the output file? (y/n) -->> ")
        if save_5 == "y":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -O -Pn -n --open -oN scan.txt")
            sys.exit(0)
        if save_5 == "n":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -O -Pn -n --open")
            sys.exit(0)
    if int(z) == 6:
        print("")
        save_6 = input("Do you want to save the output file? (y/n) -->> ")
        if save_6 == "y":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -p- -O -sVC -Pn -n --open -oN scan.txt")
            sys.exit(0)
        if save_6 == "n":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -p- -O -sVC -Pn -n --open")
            sys.exit(0)
    if int(z) == 7:
        print("")
        port = input("Select the specific port to scan -->> ")
        print("")
        save_7 = input("Do you want to save the output file? (y/n) -->> ")
        if save_7 == "y":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -p{int(port)} -sVC -Pn -n --open -oN scan.txt")
            sys.exit(0)
        if save_7 == "n":
            os.system("clear")
            os.system(f"nmap {v_ip} --min-rate 5000 -p{int(port)} -sVC -Pn -n --open")
            sys.exit(0)
    if int(z) == 8:
        print("")
        os.system("clear")
        menu()

        

menu()