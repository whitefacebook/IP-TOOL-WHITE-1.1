import os
import requests
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def slowprint(text, delay=0.008):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    clear()
    ascii_art = f"""{Fore.GREEN}
  ███╗   ██╗███████╗████████╗██╗  ██╗███████╗    ██████╗  ██████╗  ██████╗ ██╗  ██╗
  ████╗  ██║██╔════╝╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
  ██╔██╗ ██║█████╗     ██║   ███████║█████╗      ██████╔╝██║   ██║██║   ██║█████╔╝ 
  ██║╚██╗██║██╔══╝     ██║   ██╔══██║██╔══╝      ██╔═══╝ ██║   ██║██║   ██║██╔═██╗ 
  ██║ ╚████║███████╗   ██║   ██║  ██║███████╗    ██║     ╚██████╔╝╚██████╔╝██║  ██╗
  ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚══════╝    ╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                  {Fore.RED}WHITE 404 GHz {Fore.LIGHTBLACK_EX}- CyberOps Division
    """
    print(ascii_art)
    print(Fore.LIGHTBLACK_EX + "-" * 80)
    print(Fore.LIGHTWHITE_EX + "  [ TOOLS : IP Locate | Traceroute | Whois | Ping | Recon | Sys Tools ]")
    print(Fore.LIGHTBLACK_EX + "-" * 80 + "\n")

def menu():
    print(f"""{Fore.LIGHTWHITE_EX}
    [1] Localiser une IP
    [2] Voir votre IP publique
    [3] Traceroute
    [4] Ping
    [5] Whois
    [6] Outils Système & Réseau
    [7] Quitter
""")

def sys_tools_menu():
    print(f"""{Fore.LIGHTWHITE_EX}
    [1] Voir IP locale (ifconfig)
    [2] Voir connexions réseau (netstat)
    [3] Voir ports ouverts (ss)
    [4] Voir table ARP (arp -a)
    [5] Temps depuis dernier démarrage (uptime)
    [6] Utilisation CPU/RAM (top)
    [7] Utilisation stockage (df -h)
    [8] Taille du dossier courant (du -sh .)
    [9] Utilisateur actuel (whoami)
    [10] Infos système (uname -a)
    [0] Retour menu principal
    """)

def run_sys_tool(choice):
    cmds = {
        "1": "ifconfig",
        "2": "netstat -antup",
        "3": "ss -tuln",
        "4": "arp -a",
        "5": "uptime",
        "6": "top",
        "7": "df -h",
        "8": "du -sh .",
        "9": "whoami",
        "10": "uname -a"
    }
    cmd = cmds.get(choice)
    if cmd:
        os.system(cmd)
    else:
        print(f"{Fore.RED}Option invalide.")

def loading(msg="Chargement", duration=1.3):
    print(f"{Fore.LIGHTBLACK_EX}[{msg}]", end="", flush=True)
    for _ in range(3):
        time.sleep(duration / 3)
        print(".", end="", flush=True)
    print("\n")

def get_ip_info():
    ip = input(f"{Fore.LIGHTGREEN_EX}CIBLE IP > {Fore.RESET}")
    try:
        loading("Analyse")
        url = f"http://ip-api.com/json/{ip}?fields=66846719"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            print(f"\n{Fore.LIGHTWHITE_EX}--- Informations Géographiques ---\n")
            fields_to_show = ['query', 'country', 'regionName', 'city', 'zip', 'lat', 'lon', 'isp', 'org', 'as', 'mobile', 'proxy']
            for key in fields_to_show:
                print(f"{Fore.LIGHTCYAN_EX}{key.capitalize():<12}: {Fore.RESET}{data.get(key, 'N/A')}")
            lat, lon = data['lat'], data['lon']
            print(f"\n{Fore.LIGHTMAGENTA_EX}Lien Google Maps: {Fore.RESET}https://www.google.com/maps?q={lat},{lon}")
        else:
            print(f"{Fore.RED}Erreur: IP non localisable -> {data['message']}")
    except Exception as e:
        print(f"{Fore.RED}Exception : {e}")

def get_my_ip():
    try:
        loading("Récupération IP publique")
        ip = requests.get("https://api.ipify.org").text
        print(f"\n{Fore.LIGHTWHITE_EX}Votre IP publique : {Fore.LIGHTGREEN_EX}{ip}")
    except Exception as e:
        print(f"{Fore.RED}Erreur : {e}")

def traceroute():
    host = input(f"{Fore.LIGHTGREEN_EX}CIBLE > {Fore.RESET}")
    print(f"\n{Fore.LIGHTWHITE_EX}--- Traceroute vers {host} ---\n")
    os.system(f"traceroute {host}")

def ping():
    host = input(f"{Fore.LIGHTGREEN_EX}CIBLE > {Fore.RESET}")
    print(f"\n{Fore.LIGHTWHITE_EX}--- Ping vers {host} ---\n")
    os.system(f"ping -c 4 {host}")

def whois_lookup():
    target = input(f"{Fore.LIGHTGREEN_EX}CIBLE > {Fore.RESET}")
    print(f"\n{Fore.LIGHTWHITE_EX}--- WHOIS pour {target} ---\n")
    os.system(f"whois {target}")

def main():
    while True:
        banner()
        menu()
        choice = input(f"{Fore.LIGHTYELLOW_EX}SÉLECTION > {Fore.RESET}")

        if choice == '1':
            get_ip_info()
        elif choice == '2':
            get_my_ip()
        elif choice == '3':
            traceroute()
        elif choice == '4':
            ping()
        elif choice == '5':
            whois_lookup()
        elif choice == '6':
            while True:
                sys_tools_menu()
                sub_choice = input(f"{Fore.LIGHTYELLOW_EX}SÉLECTION OUTIL > {Fore.RESET}")
                if sub_choice == '0':
                    break
                run_sys_tool(sub_choice)
                input(f"\n{Fore.LIGHTBLACK_EX}Appuyez sur Entrée pour continuer...")
        elif choice == '7':
            print(f"\n{Fore.RED}Fermeture...")
            time.sleep(1)
            break
        else:
            print(f"{Fore.RED}Option invalide.")

        input(f"\n{Fore.LIGHTBLACK_EX}Appuyez sur Entrée pour revenir au menu...")

if __name__ == "__main__":
    main()
