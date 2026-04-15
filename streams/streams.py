import io
import struct

class PacienteOutputStream(io.RawIOBase):
    def __init__(self, pacientes, n_objetos, destino):
        self.pacientes = pacientes[:n_objetos]
        self.destino = destino

    def enviar_dados(self):
        for p in self.pacientes:
            # 1. Transformar atributos em bytes
            nome_bytes = p.nome.encode('utf-8')
            especie_bytes = p.especie.encode('utf-8')
            
            # 2. Preparar os tamanhos (Header)
            header = struct.pack('!III', p.id_animal, len(nome_bytes), len(especie_bytes))
            
            # 3. Escrever no destino
            self.destino.write(header)
            self.destino.write(nome_bytes)
            self.destino.write(especie_bytes)
            self.destino.flush()