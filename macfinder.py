import re
import subprocess
import sys

def get_manufacturer(macadress):
    if not re.match(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", macadress):
        print("Invalid MAC format.")
        return
    mac_prefix = macadress[:8   ].replace(":", "").upper()
    try:
        result = subprocess.run(
            ["grep", "-i", mac_prefix, "/usr/share/arp-scan/ieee-oui.txt"],
            capture_output=True, text=True
        )
        if result.stdout:
            fabricante = result.stdout.split(None, 1)[1].strip()
            print(fabricante)
        else:
            print("Manafacturer not found.")
    except FileNotFoundError:
        print("ieee-oui.txt not found. You must install arp-scan.")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <MAC>")
        sys.exit(1)
    get_manufacturer(sys.argv[1])
