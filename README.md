# Trabalho 1: Sistemas Distribuídos - Comunicação entre Processos
> **Comunicação entre Processos (IPC) & Serialização Manual** > *Universidade Federal do Ceará – Campus Quixadá*
Disciplina: Sistemas Distribuídos
Docente: Antônio Rafael Braga
Discentes: Alfredo Borges do Nascimento Neto | Gessyca de Oliveira Cunha

Este projeto implementa os conceitos de comunicação entre processos (IPC), manipulação de fluxos de dados (Streams) e serialização manual, aplicados a um serviço de **Consultório Veterinário**.

## Como Executar
### Pré-requisitos
* Python 3.10 ou superior.

### Passo a Passo
1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/sd-consultorio.git
   cd sd-consultorio
   ```
2. **Executar Testes de Serialização:**
   ```bash
   python main.py
   ```
3. **Executar Alertas Multicast (UDP):**
   * Abra um terminal para o cliente: `python usuarios/cliente.py`
   * Abra outro terminal para o administrador: `python usuarios/admin_multicast.py`

---

### 1. Definição do Serviço e POJOs
* **O que foi feito:** Definição do serviço de **Gestão de Consultório**.
* **Implementação:** No arquivo `pojos.py`, foram criadas as classes `Paciente` e `Consulta`.
* **Conceito:** Essas classes representam objetos simples (POJOs em Java, ou Data Classes em Python) que servem de estrutura para o tráfego de informações no sistema distribuído.

### 2. Implementação de OutputStream Personalizado
* **O que foi feito:** Criação da classe `PacienteOutputStream` que herda de `io.RawIOBase` (equivalente ao `OutputStream` do Java).
* **Regras Seguidas:**
    * **(i)** Recebe um array de objetos `Paciente`.
    * **(ii)** Recebe o número de objetos a serem transmitidos.
    * **(iii)** Envia metadados fixos (Header) contendo o ID (4 bytes), Nome (4 bytes) e Espécie (4 bytes).
    * **(iv)** Direciona os dados para um `destino` (qualquer objeto que suporte o método `.write()`).

### 3. Testes de Destino
A implementação foi validada no arquivo `main.py` cobrindo três cenários:
1.  **Saída Padrão:** Utilizando `sys.stdout.buffer` para enviar os bytes diretamente para o terminal.
2.  **Arquivo:** Utilizando `open("dados.bin", "wb")` para persistir o fluxo de bytes em disco.
3.  **Remoto (TCP):** A arquitetura permite passar um objeto de socket como `destino`.

---

## 🛠️ Detalhes da Serialização (Representação Externa de Dados)

Para garantir que os dados sejam compreendidos por qualquer processo (independente da arquitetura da CPU), utilizamos o módulo `struct` do Python com a convenção **Network Byte Order (Big-Endian)** denotada pelo prefixo `!`.

**Estrutura do Pacote de Bytes (Frame):**

| Campo | Tipo | Tamanho | Descrição |
| :--- | :--- | :--- | :--- |
| **ID** | Inteiro | 4 bytes | Identificador único do animal |
| **Tam_Nome** | Inteiro | 4 bytes | Quantidade de bytes do nome |
| **Tam_Especie**| Inteiro | 4 bytes | Quantidade de bytes da espécie |
| **Nome** | String | Variável | Nome do animal em UTF-8 |
| **Especie** | String | Variável | Espécie do animal em UTF-8 |

### 5. Comunicação Multicast (Notas Informativas)
* **O que foi feito:** Implementação de um canal de avisos do administrador para os clientes.
* **Tecnologia:** UDP Multicast (Grupo IP `224.1.1.1`, Porta `5007`).
* **Lógica:** * O **Administrador** (Sender) envia mensagens Unidirecionais.
    * O **Cliente** (Receiver) se inscreve no grupo de IGMP para receber notificações em tempo real.
* **Exemplo de Uso:** Envio de alertas de manutenção ("Sistema temporariamente fora de serviço").