import subprocess

obtain_ip = subprocess.run(
    "ip a | grep 'inet ' | awk '{print $2}' | cut -d/ -f1 | grep -v 127.0.0.1",
    shell=True,
    capture_output=True,
    text=True
)
local_ip = obtain_ip.stdout.strip()


subprocess.run(["xclip", "-selection", "clipboard"], input=f"http://{local_ip}:8080/", text=True)
print()
print(f"Your local ip is: {local_ip}, access by: \033[92mhttp://{local_ip}:8080/\033[92m")
print()
print("\033[93mStarting server. Press Ctrl+C to stop.\033[93m\033[97m\033[97m")
print()
try:
    while True:
        subprocess.Popen(
    ["python3", "-m", "http.server", "8080"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
    )
except KeyboardInterrupt:
    print("\nServer closed.")
    exit()