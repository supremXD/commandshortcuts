import os, sys, subprocess

def get_interfaces_with_ip():
	output = []
	for interface in sorted(os.listdir("/sys/class/net")):
		if interface == "lo":
			continue
		getip = subprocess.run(
			["ip", "-4", "-br", "addr", "show", interface],
			capture_output=True,
			text=True
		)
		parts = getip.stdout.split()
		ip = parts[2].split("/")[0] if len(parts) >= 3 else "unassigned"
		output.append((interface, ip))
	return output


output = get_interfaces_with_ip()

if len(sys.argv) == 1:
	for interface, ip in output:
		print(f"{interface:<15} ({ip})")



if len(sys.argv) >= 2:
	option = sys.argv[1]
	if option == "-c":
		clipboard = ""
		for interface, ip in output:
			clipboard += f"{interface} "
			subprocess.run(["xclip", "-selection", "clipboard"], input=clipboard, text=True)
	else:
		print("unknow option")
