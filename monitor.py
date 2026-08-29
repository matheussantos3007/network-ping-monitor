import subprocess
import threading
import time
from datetime import datetime

# Lista de IPs do Provedor para monitorar (Exemplos)
ATIVOS = {
    "Roteador Principal": "8.8.8.8",
    "Servidor DNS": "1.1.1.1",
    "Switch Central": "192.168.1.1"
}

def ping_host(nome, ip):
    # Executa o comando ping (1 pacote, timeout de 2 segundos)
    comando = ["ping", "-c", "1", "-W", "2", ip]
    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if resultado.returncode == 0:
        print(f"[{timestamp}] ✅ {nome} ({ip}) está ONLINE.")
    else:
        print(f"[{timestamp}] 🚨 ALERTA: {nome} ({ip}) está OFFLINE!")

def iniciar_monitoramento():
    print("🚀 Iniciando monitoramento de ativos...")
    threads = []
    
    for nome, ip in ATIVOS.items():
        thread = threading.Thread(target=ping_host, args=(nome, ip))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    iniciar_monitoramento()
