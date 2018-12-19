# -*- coding: utf-8 -*-

# servidor TCP
import socket # Biblioteca de sockets em Python
import threading

ip = '127.0.0.1' # ou ip = ''0.0.0.0
porta = 5000

# AF_INET diz que estou usando IPv4.
# SOCK_STREAM diz que estou fazendo uma aplicação TCP.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, porta))
server.listen(1) # número de portas sendo escutadas
print('Ouvindo em {}:{}'.format(ip, porta))

def cliente(cliente_socket):
    resposta1 = cliente_socket.recv(1024) # resposta recebe o que o cliente enviou.
    print('Resposta: {}'.format(resposta1))
    cliente_socket.send("Chegou!")
    cliente_socket.close()

while True:
    client, addr = server.accept()
    print('Conexão recebida por {}:{}'.format(addr[0], addr[1]))
    cliente = threading.Thread(target=cliente, args=(cliente,))
    cliente.start()

