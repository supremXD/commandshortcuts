import os, sys

def get_network_interface():
    interfaces = [
        i for i in os.listdir("/sys/class/net")
        if i != "lo"
    ]
    return interfaces[0] if interfaces else None

interface = get_network_interface()

if len(sys.argv) == 1:
	print(interface)
elif len(sys.argv) >= 2:
	option = sys.argv[1]
	if option == "-c":
		print(interface)
		os.system(f"echo -n {interface} | xclip -selection clipboard")
	else:
		print("unknow option")
