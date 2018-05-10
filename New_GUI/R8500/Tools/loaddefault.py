from API._API import *
import os
import subprocess

aploaddefault()

status = os.system("ping -n 2 192.168.1.1")
if status == 1:
    print("Release LAN")
    os.system("netsh interface set interface \"LAN\" disabled")
    time.sleep(10)
    print("Reload LAN")
    os.system("netsh interface set interface \"LAN\" enabled")
    time.sleep(10)
    
    
