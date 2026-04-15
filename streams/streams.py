import io
import struct

class PacienteOutputStream(io.RawIOBase):
    def __init__(self, pacientes, n_objetos, destino):
        self.pacientes = pacientes[:n_objetos]
        self.destino = destino

    def enviar_dados(self, debug=True):
        for p in self.pacientes:
            nome_bytes = p.nome.encode('utf-8')
            especie_bytes = p.especie.encode('utf-8')
            
            header = struct.pack('!III', p.id_animal, len(nome_bytes), len(especie_bytes))
            pacote = header + nome_bytes + especie_bytes
            
            if debug:
                hex_dump = pacote.hex(' ').upper()
                print(f"Objeto [{p.nome} | {p.especie}]: {hex_dump}")
            
            self.destino.write(pacote)
            self.destino.flush()