import socket
import time

# Cria um objeto de socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
endereco_servidor = ('127.0.0.1', 12345)
cliente_socket.connect(endereco_servidor)

# Envia três mensagens diferentes
mensagens = ["Mensagem 1", "Mensagem 2", "Mensagem 3", "break"]

for mensagem in mensagens:
    cliente_socket.sendall(mensagem.encode())
    print(f"Enviado para o servidor: {mensagem}")
    time.sleep(1)  # Aguarda um segundo entre mensagens

# Fecha a conexão
cliente_socket.close()
