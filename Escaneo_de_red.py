import socket
import ipaddress
from datetime import datetime
from colorama import Fore, Style, init

# Inicializar colorama
init()

# Puertos a escanear
PORTS = [21, 22, 23, 80, 443, 445, 389, 636, 3268, 3269, 1433, 3389]

# Función para escanear puertos en una IP específica
def scan_ports(ip):
    open_ports = []
    for port in PORTS:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((str(ip), port))
            if result == 0:
                open_ports.append(port)
    return open_ports

# Función principal de escaneo de red
def network_scan(start_ip, end_ip):
    start_time = datetime.now()

    print(Fore.CYAN + "\nIniciando el escaneo..." + Style.RESET_ALL)
    start_ip = ipaddress.IPv4Address(start_ip)
    end_ip = ipaddress.IPv4Address(end_ip)

    # Abrir el archivo en modo de escritura en tiempo real
    with open("resultado_de_escaneo_de_la_red.txt", "w") as file:
        file.write("Resultado del escaneo de la red:\n")
        file.write("Fecha de escaneo: " + str(start_time) + "\n\n")

        # Iterar en el rango de IPs
        for ip in range(int(start_ip), int(end_ip) + 1):
            ip_addr = ipaddress.IPv4Address(ip)
            print(Fore.YELLOW + f"Escaneando IP: {ip_addr}" + Style.RESET_ALL)
            open_ports = scan_ports(ip_addr)
            
            if open_ports:
                open_ports_str = ', '.join(map(str, open_ports))
                print(Fore.GREEN + f"[*] IP {ip_addr} - Puertos abiertos: {open_ports_str}" + Style.RESET_ALL)
                
                # Escribir el resultado en el archivo inmediatamente
                file.write(f"IP {ip_addr} - Puertos abiertos: {open_ports_str}\n")
        
        end_time = datetime.now()
        duration = end_time - start_time
        file.write("\nDuración del escaneo: " + str(duration) + "\n")
    
    print(Fore.CYAN + f"\nEscaneo completo. Duración: {duration}" + Style.RESET_ALL)

# Función para imprimir el banner
def print_banner():
    print(Fore.MAGENTA + """
****************************************
  Este script escaneará la red local
  en busca de puertos comunes abiertos.
""" + Fore.YELLOW + "  https://pentestingcampa.cl" + Fore.MAGENTA + """
  
""" + Fore.GREEN + """  Uso:
    Archivo de salida final: python3 Escaneo_de_red.py
    Archivo de salida inmediato sin mensaje de consola: python3 Escaneo_de_red.py > resultado.txt
****************************************
""" + Style.RESET_ALL)

if __name__ == "__main__":
    print_banner()
    network_scan("192.168.1.1", "192.168.255.255")
