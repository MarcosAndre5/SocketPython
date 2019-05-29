# -*- coding: utf-8 -*-
'''
    ALUNOS: Marcos André Azevedo de Assis e Althierfson Tullio Azevedo de Lima.
    TRABALHO: Chat Cliente/Servidor MultThread com Socket usando modeldo TCP.
    DISCIPLINA: Sistemas Distribuídos.
    Python versão: 3.7.
    DATA: 28/05/2019.
'''
from _thread import *
from socket import *
import time

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
            print('Tentando novamente em 1 segundos\n')
            time.sleep(1)

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
            print('Tente em 1 segundos\n')
            time.sleep(1)

def receber(s):
    while True:
        try:
            reply = s.recv(2048)
            print(reply.decode('UTF-8'))
            break
        except:
            print('\nNão foi possível receber resposta')
            print('Tente em 1 segundos\n')
            time.sleep(1)

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
    print('\nConexão com o Servidor estabelecida!\nServidor: ', ip + ' : ' + str(porta)+ '\n')
    print('Escreva suas mensagens:\n')
    start_new_thread(enviar,(s,))
    while exit != True:
        pass
    print("\nDesculpe, algo deu errado! Você perdeu a conexão com o servidor.")
    print("Fechando a janela em 5 segundos.")
    time.sleep(5)
main()
