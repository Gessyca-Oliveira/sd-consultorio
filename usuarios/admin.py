import socket
import struct

def enviar_aviso(mensagem):
    multicast_group = ('224.1.1.1', 5007)
    
    # Criando o socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # TTL de 1 significa que a mensagem não sai da rede local
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    try:
        print(f"Enviando nota: {mensagem}")
        sock.sendto(mensagem.encode('utf-8'), multicast_group)
    finally:
        sock.close()

if __name__ == "__main__":
    msg = "AVISO: Sistema temporariamente fora de serviço para manutenção às 22:00."
    enviar_aviso(msg)