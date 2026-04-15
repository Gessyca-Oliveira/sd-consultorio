import sys
from pojos.paciente import Paciente
from streams.streams import PacienteOutputStream

def executar_testes():
    pacientes = [
        Paciente(101, "Luna", "Cao"),
        Paciente(202, "Nani", "Gato"),
        Paciente(203, "Theo", "Gato"),
    ]

    print("=== TESTE 1: ENVIANDO PARA O CONSOLE (System.out) ===")
    stream_console = PacienteOutputStream(pacientes, 3, sys.stdout.buffer)
    stream_console.enviar_dados()
    print("\n\n=== TESTE 2: ENVIANDO PARA ARQUIVO (dados.bin) ===")
    
    with open("dados.bin", "wb") as arquivo:
        stream_arquivo = PacienteOutputStream(pacientes, 3, arquivo)
        stream_arquivo.enviar_dados()
    
    print("Arquivo 'dados.bin' gerado com sucesso!")

if __name__ == "__main__":
    executar_testes()