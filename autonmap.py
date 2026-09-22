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


if os.geteuid() != 0:
    print('This scrips needs to be executed with root privileges. Try "sudo python3 autonmap.py"')
    sys.exit(1)


def menu():
    os.system("clear")
    print(banner)
    print("")
    print("              |                    1-->> Scan full network")
    print("              |                    2-->> Scan IP")
    print("              |                    3-->> MAC finder and scanner")
    print("              |                    4-->> Exit")
    x = input("              ↳ ")

    if int(x) == 1:
        scan()

    if int(x) == 2:
        attack()

    if int(x) == 3:
        macfinder()

    if int(x) == 4:
        os.system("clear")
        print("Goodbye :)")
        sys.exit(0)


def scan():
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
    print("              |                    2-->> Export in .txt")
    print("              |                    3-->> Export in .xml")
    print("              |                    4-->> Export in script kiddie")
    print("              |                    5-->> Export in grepable")
    print("              |                    6-->> Return")
    print("              |                    7-->> Exit")               
    x = input("              ↳ ")
    if int(x) == 1:
        os.system("clear")
        os.system(f"nmap {network} --min-rate 5000 -Pn -n --open")
        sys.exit(0)
    if int(x) == 2:
        export_option = "-oN"
    if int(x) == 3:
        export_option = "-oX"
    if int(x) == 4:
        export_option = "-oS"
    if int(x) == 5:
        export_option = "-oG"
    if int(x) == 6:
        menu()
    if int(x) == 7:
        os.system("clear")
        print("Goodbye :)")
        sys.exit(0)
    os.system("clear")
    os.system(f"nmap {network} --min-rate 5000 -Pn -n --open {export_option} scan.txt")
    os.system("clear")
    os.system("sed -i '/RTTVAR/d' scan.txt")
    print("Scan saved as scan.txt")
    print("")
    print("Goodbye :)")
    sys.exit(0)


def attack():
    print("")
    victim_ip= input("Place the ip to scan here -->> ").strip()
    parts = victim_ip.split(".")
    if len(parts) != 4:
        print("Invalid IP format. Must be a.b.c.d (For example: 192.168.1.150)")
        time.sleep(3)
        menu()
    else:
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
        print("              |                    9-->> Exit")
        x = input("              ↳ ")
        if int(x) == 8:
                    os.system("clear")
                    menu()
        if int(x) == 9:
                    os.system("clear")
                    print("Goodbye :)")
                    sys.exit(0)
        os.system("clear")
        print("")
        save = input('Do you want to save the output file as "target.txt"? (y/n) -->> ').strip().lower()

        if save == "y":
            option = " -oN target.txt"

        if save == "n":
            option = ""
        os.system("clear")

        if int(x) == 1:
            os.system(f"nmap {victim_ip} --min-rate 5000 -Pn -n --open{option}")

        if int(x) == 2:
            os.system(f"nmap {victim_ip} --min-rate 5000 -p- -Pn -n --open{option}")

        if int(x) == 3:
            os.system(f"nmap {victim_ip} --min-rate 5000 -p- -sV -Pn -n --open{option}")

        if int(x) == 4:
            os.system(f"nmap {victim_ip} --min-rate 5000 -p- -sC -Pn -n --open{option}")

        if int(x) == 5:
            os.system(f"nmap {victim_ip} --min-rate 5000 -O -Pn -n --open{option}")

        if int(x) == 6:
            os.system(f"nmap {victim_ip} --min-rate 5000 -p- -O -sVC -Pn -n --open{option}")

        if int(x) == 7:
            print("")
            port = input("Select the specific port to scan -->> ")
            os.system("clear")
            os.system(f"nmap {victim_ip} --min-rate 5000 -p{int(port)} -sVC -Pn -n --open{option}")

        os.system("sed -i '/RTTVAR/d' target.txt")
        print("")
        print("Goodbye :)")
        sys.exit(0)


def macfinder():
    os.system("clear")
    print(banner)
    print("")
    print("              |                    1-->> Find MAC with nmap")
    print("              |                    2-->> Find MAC with arp-scan")
    print("              |                    3-->> Scan MAC for information about it")
    print("              |                    4-->> Return")
    print("              |                    5-->> Exit")
    x = input("              ↳ ")

    if int(x) == 1:
        os.system("clear")
        print("")
        save = input('Do you want to save the output file as "mac.txt"? (y/n) -->> ').strip().lower()
        if save == "y":
            option = " -oN mac.txt"
        if save == "n":
            option = ""
        os.system("clear")
        print("")
        ip = input("IP to scan for its MAC address-->> ")
        os.system("clear")
        os.system(f"nmap {ip} -sn -n{option}")
        os.system("sed -i '/RTTVAR/d' mac.txt")
        print("")
        print("Goodbye :)")
        sys.exit(0)

    if int(x) == 2:
        os.system("clear")
        print("")
        save = input('Do you want to save the output file as "mac.txt"? (y/n) -->> ').strip().lower()
        if save == "y":
            option = " | tee mac.txt"
        if save == "n":
            option = ""
        os.system("clear")
        print("")
        ip = input("IP to scan for its MAC address-->> ")
        os.system("clear")
        os.system(f"arp-scan {ip}{option}")
        print("")
        print("Goodbye :)")
        sys.exit(0)

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
            mac = input("MAC address to scan-->> ")
            os.system(f"python3 {file} {mac}")

    if int(x) == 4:
        menu()

    if int(x) == 5:
        os.system("clear")
        print("Goodbye :)")
        sys.exit(0)


menu()
