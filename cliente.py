# -*- coding: utf-8 -*-

# cliente TCP
import socket #Biblioteca de sockets em Python

host = '127.0.0.1' #localhost
porta = 9999

# AF_INET diz que estou usando IPv4.
# SOCK_STREAM diz que estou fazendo uma aplicação TCP.
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, porta)) # Conectando ao servidor
cliente.send('Conectou!')
resposta = cliente.recv(1024)
print(resposta)
