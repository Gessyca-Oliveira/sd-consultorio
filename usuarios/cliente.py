import socket
import struct

def iniciar_ouvinte_multicast():
    multicast_group = '224.1.1.1'
    server_address = ('', 5007) # Ouve em todas as interfaces na porta 5007

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    # Diz ao sistema operacional para adicionar o socket ao grupo multicast
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print(" Aguardando notas informativas do administrador...")

    while True:
        data, address = sock.recvfrom(1024)
        print(f"\n NOTA RECEBIDA: {data.decode('utf-8')}")

if __name__ == "__main__":
    iniciar_ouvinte_multicast()