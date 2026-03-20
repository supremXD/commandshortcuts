import subprocess, sys

obtain_ip = subprocess.run(
    "ip a | grep 'inet ' | awk '{print $2}' | cut -d/ -f1 | grep -v 127.0.0.1",
    shell=True,
    capture_output=True,
    text=True
)
ip = obtain_ip.stdout.strip()

if len(sys.argv) == 1:
    print(ip)
elif len(sys.argv) >= 2:
    option = sys.argv[1]
    if option == "-c":
        subprocess.run(["xclip", "-selection", "clipboard"], input=f"{ip}", text=True)
    elif option == "-http":      
        subprocess.run(["xclip", "-selection", "clipboard"], input=f"http://{ip}:8080/", text=True)
    elif option in ("-h", "-help", "--help"):
        print("""
        Options:
        -c : Copy your local IP.
        -http : Copy "http://your_local_ip:8080/.
        -h/-help/--help : Show this message.
        """)
    else:
        print("Unknown option, use -h for help.")