from os import system as c
import time
import random

#------------- COLOUR ------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{G}
 ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄ 
▐▌  ▐▌ ▄     ▀▄  ▀ ▄     ▐▌  ▐▌
▐▛▀▀▀▌ █ ▄▄▄  █     ▀▄▄▄ ▐▛▀▀▀▌
▐▌  ▐▌ ▀▄▄▄▀ ▄▄▀   ▀▄▄▄▀ ▐▌  ▐▌
{P} HACKING WORLD - WIFI CONNECT VIP TOOL
""")

#------------- WIFI HACK -------------#
def wifi_hack():
    logo()
    c('espeak "WiFi Connect Tool Starting"')
    wifi_uid = input(f"{Y}Enter WiFi name: ")

    print(f"\n{C}[+] Scanning Nearby Networks...")
    time.sleep(2)
    print(f"{G}[✓] WiFi UID Found: {wifi_uid}")
    time.sleep(1)

    print(f"{B}[+] Connecting To {wifi_uid}...\n")
    time.sleep(1)

    # Signal Animation
    for i in range(1, 6):
        print(f"{C}[{'='*i}>{' '*(5-i)}] Connecting... {i*20}%")
        time.sleep(1)

    print(f"\n{G}[✓] Connected To {wifi_uid} Successfully!\n")
    print(f"{Y}[+] Cracking Password...")
    time.sleep(2)

    # Fake Passwords
    passwords = ['wifi12345', '12345678', 'hackwifi2024', 'adminwifi', 'password2025']
    for pw in passwords:
        print(f"{C}[*] Found: {pw}")
        time.sleep(1)

    print(f"\n{R}[!] Session Expired! Root Permission Required To Continue.\n")
    time.sleep(1)
    print(f"{Y}Please Restart Tool With Root Access!\n")
    input(f"{A}Press Enter To Exit...")

#------------- START TOOL -------------#
wifi_hack()