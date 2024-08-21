import requests
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Banner "C4mp4 Check Headers"
def print_banner():
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
       _..._                                                                  _____      
    .-'_..._''.                                                              /    /      
  .' .'      '.\             __  __   ___    _________   _...._             /    /       
 / .'                       |  |/  `.'   `.  \        |.'      '-.         /    /        
. '                         |   .-.  .-.   '  \        .'```'.    '.      /    /         
| |                  __     |  |  |  |  |  |   \      |       \     \    /    /  __      
| |               .:--.'.   |  |  |  |  |  |    |     |        |    |   /    /  |  |     
. '              / |   \ |  |  |  |  |  |  |    |      \      /    .   /    '   |  |     
 \ '.          . `" __ | |  |  |  |  |  |  |    |     |\`'-.-'   .'   /    '----|  |---. 
  '. `._____.-'/  .'.''| |  |__|  |__|  |__|    |     | '-....-'`    /          |  |   | 
    `-.______ /  / /   | |_                    .'     '.             '----------|  |---' 
             `   \ \._,\ '/                  '-----------'                      |  |     
                  `--'  `"                                                     /____\  
                  
{Style.RESET_ALL}
                   {Fore.GREEN}Camp4 Check Headers \n https://pentestingcampa.cl/{Style.RESET_ALL}
    """
    print(banner)

# Lista de cabeceras de seguridad recomendadas por OWASP que deben estar presentes
SECURITY_HEADERS = {
    "Strict-Transport-Security": "Strict-Transport-Security header is not set!",
    "X-Frame-Options": "X-Frame-Options header is not set!",
    "X-Content-Type-Options": "X-Content-Type-Options header is not set!",
    "Content-Security-Policy": "Content-Security-Policy header is not set!",
    "X-Permitted-Cross-Domain-Policies": "X-Permitted-Cross-Domain-Policies header is not set!",
    "Referrer-Policy": "Referrer-Policy header is not set!",
    "Clear-Site-Data": "Clear-Site-Data header is not set!",
    "Cross-Origin-Embedder-Policy": "Cross-Origin-Embedder-Policy header is not set!",
    "Cross-Origin-Opener-Policy": "Cross-Origin-Opener-Policy header is not set!",
    "Cross-Origin-Resource-Policy": "Cross-Origin-Resource-Policy header is not set!",
    "Cache-Control": "Cache-Control header is not set!"
}

# Lista de cabeceras que no deben estar presentes
DISALLOWED_HEADERS = [
    "Feature-Policy",
    "Expect-CT",
    "Public-Key-Pins",
    "X-XSS-Protection",
    "Pragma"
]

def analyze_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        print(f"Analyzing security headers for {url}\n")
        
        # Verificar cabeceras recomendadas
        for header, warning in SECURITY_HEADERS.items():
            print("-" * 50)
            if header in headers:
                print(Fore.GREEN + f"{header}: {headers[header]}")
            else:
                print(Fore.RED + f"{header}: {warning}")
        
        print("\nChecking for disallowed headers...\n")
        
        # Verificar cabeceras no recomendadas
        for header in DISALLOWED_HEADERS:
            print("-" * 50)
            if header in headers:
                print(Fore.RED + f"Warning: {header} header should not be used! Found: {headers[header]}")
            else:
                print(Fore.GREEN + f"{header}: Not present (Correct)")
        
        print("-" * 50)  # Final separator for clarity
        
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error fetching {url}: {e}")

if __name__ == "__main__":
    print_banner()
    url = input("Enter the URL to analyze: ")
    if not url.startswith("http"):
        url = "http://" + url
    analyze_security_headers(url)
