# -*- coding: utf-8 -*-
'''
    ALUNO: Marcos André Azevedo de Assis
    DISCIPLINA: Redes de Computadores
    TRABALHO: Chat Cliente/Servidor com Socket usando modeldo TCP.
    DATA: 03/10/2018
    Python versão 3.7
'''
from socket import *
import time
from _thread import *

def endereco(): # Pede o IP e porta de destino
    print('\t CLIENTE')
    ip = input('Endereço do Servidor: ')
    porta = int(input('PORTA: '))
    return ip, porta

def criarSocket(): # Criando o socket usando IPv4 e modelo TCP 
    s = socket(AF_INET, SOCK_STREAM)
    return s

def conectar(ip, porta, s):
    s.connect((ip, porta))

def tentarConexao(ip, porta, s):
    while True:
        print('\nTentando se conectar a:', ip + ' : ' + str(porta))
        try:
            conectar(ip, porta, s)
            break
        except:
            print('Não há servidor em: ', ip + ' : ' + str(porta))
            print('Tentando novamente em 5 segundos\n')
            time.sleep(5)

def enviar(s):
    while True:
        global exit
        try:
            msg = input('')
            msg = client + ' : ' + msg
            if msg == client + ' : sair':
                exit = True
                msg = 'O cliente ' + client + ' saiu.'
                s.send(msg.encode('UTF-8'))
                s.close
                break
            else:
                s.send(msg.encode('UTF-8'))
                start_new_thread(receber,(s,))
        except:
            print('\nAlgo aconteceu')
            print('Tente em 5 segundos\n')
            time.sleep(5)

def receber(s):
    while True:
        try:
            reply = s.recv(2048)
            print(reply.decode('UTF-8'))
            break
        except:
            print('\nNão pode receber resposta')
            print('Tente em 5 segundos\n')
            time.sleep(5)

def receberEspecial(s):
    global client
    client = s.recv(2048).decode("UTF-8")

exit = False
client = ''

def main():
    ip, porta = endereco()
    s = criarSocket()
    tentarConexao(ip, porta, s)
    receberEspecial(s)
    print('\nConexão com o Servidor estabilizada!\nO Servidor é: ', ip + ' : ' + str(porta)+ '\n')
    print('Escreva suas mensagens:\n')
    start_new_thread(enviar,(s,))
    while exit != True:
        pass
    print("\nDesculpe, algo deu errado! Você perdeu a conexão com o servidor.")
    print("Fechando a janela em 5 segundos.")
    time.sleep(10)
main()


