import socket
import random

# Cria um objeto de socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket a um endereço e porta específicos
endereco_servidor = ('127.0.0.1', 12345)
server_socket.bind(endereco_servidor)

# Escuta por conexões entrantes
server_socket.listen(1)

print("Servidor está aguardando conexões...")


def generate_random_id():
    return random.randint(1000, 9999)


while True:
    # Aguarda por uma conexão
    conexao_cliente, endereco_cliente = server_socket.accept()
    print(f"Conexão de: {endereco_cliente}")

    while True:
        # Recebe dados do cliente
        dados = conexao_cliente.recv(1024).decode()

        if not dados:
            print("Conexão fechada pelo cliente.")
            break

        print(f"Recebido do cliente: {dados}")

        # Gera um ID aleatório
        random_id = generate_random_id()

        # Envia o ID como resposta
        resposta = f"ID: {random_id}"
        conexao_cliente.sendall(resposta.encode())
        print(f"Enviado para o cliente: {resposta}")

    # Fecha a conexão
    conexao_cliente.close()
    print("Conexão fechada.")
