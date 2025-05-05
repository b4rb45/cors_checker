import requests
from colorama import Fore, Style, init
from pyfiglet import figlet_format
import argparse
import sys

# Inicializar colorama para colores en la terminal
init(autoreset=True)

def banner():
    print(Fore.MAGENTA + figlet_format("CORS CHECKER") + Style.RESET_ALL)

# Función para verificar configuración de CORS
def check_cors_vulnerability(url, auth_token=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Origin": "https://evil.com"  # Simulación de origen malicioso
    }

    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        acao = response.headers.get("Access-Control-Allow-Origin")
        acac = response.headers.get("Access-Control-Allow-Credentials")

        print(f"\n🔍 Verificando CORS en {url}...\n")

        print(f"{Fore.CYAN}--- [Solicitud Enviada] ---{Style.RESET_ALL}")
        for key, value in headers.items():
            print(f"{Fore.CYAN}{key}: {value}{Style.RESET_ALL}")

        print(f"\n{Fore.BLUE}--- [Respuesta del Servidor] ---{Style.RESET_ALL}")
        for key, value in response.headers.items():
            print(f"{Fore.BLUE}{key}: {value}{Style.RESET_ALL}")

        print("\n--- [Análisis de Seguridad] ---\n")

        if acao == "*":
            print(f"{Fore.RED}[X] Vulnerabilidad grave: ACAO permite cualquier origen (*).{Style.RESET_ALL}")
        elif acao == "https://evil.com":
            print(f"{Fore.YELLOW}[!] Posible mala configuración: ACAO refleja el origen del atacante ({acao}).{Style.RESET_ALL}")
        elif acao:
            print(f"{Fore.GREEN}[✔] Seguro: ACAO restringe el acceso a: {acao}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}[✔] Seguro: No expone ACAO en la respuesta.{Style.RESET_ALL}")

        if acac == "true":
            if acao == "*":
                print(f"{Fore.RED}[X] Vulnerabilidad crítica: ACAO '*' junto a ACAC 'true'.{Style.RESET_ALL}")
            elif acao == "https://evil.com":
                print(f"{Fore.RED}[X] Posible explotación: ACAO refleja origen atacante y ACAC true.{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[!] Advertencia: ACAC true puede ser riesgoso con orígenes amplios ({acao}).{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}[✔] Seguro: ACAC no permite compartir credenciales.{Style.RESET_ALL}")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[-] Error al acceder a {url}: {e}{Style.RESET_ALL}")

def get_args():
    parser = argparse.ArgumentParser(description="Herramienta para detectar CORS misconfigurations.")
    parser.add_argument("-u", "--url", required=True, help="URL objetivo a analizar")
    parser.add_argument("-t", "--token", required=False, help="Token Bearer (sin 'Bearer')")
    return parser.parse_args()

if __name__ == "__main__":
    banner()
    args = get_args()
    check_cors_vulnerability(args.url, args.token)
