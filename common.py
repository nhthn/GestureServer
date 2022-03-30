import subprocess

tmp = subprocess.run(["ip", "route", "get", "1.2.3.4"], check=True, capture_output=True)
PRIVATE_IP_ADDRESS = str(tmp.stdout).split(" ")[6]

WEBSOCKETS_PORT = 8765
