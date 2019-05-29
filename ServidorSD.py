# -*- coding: utf-8 -*-
'''
    ALUNO: Marcos André Azevedo de Assis
    DISCIPLINA: Redes de Computadores
    TRABALHO: Chat Cliente/Servidor com Socket usando modeldo TCP.
    DATA: 03/10/2018
    Python versão 3.7
'''
from socket import *
from _thread import *
import time
import sys

def endereco(): # Pede o IP e porta de destino
    print('\t SERVIDOR')
    ip = '127.0.0.1'
    porta = 5555
    return ip, porta

def criarSocket(): # Criando o socket usando IPv4 e modelo TCP 
    s = socket(AF_INET, SOCK_STREAM)
    return s 

def testarSocket(s, ip, porta): # Teste se ocorreu tudo certo na criação do socket
    while True:
        try:
            s.bind((ip, porta))
            break
        except error as e:
            print('ERRO: ', e)

#def conectar(s): # Esta ouvindo o determinado endereço
 #   conn, addr = s.accept()
  #  print('\nConexão Estabelecida.\nO Cliente é:', addr[0] + ' : ' + str(addr[1]) + '\n')
   # return conn, addr
'''

def enviarMensagem(conn): # Enviando mensagens de resposta ao cliente 1 estabelecido
    msg = input('')
    msg = '\nServidor: ' + msg
    try:
        conn.send(msg.encode('UTF-8'))
    except:
        print('\nAlgo aconteceu')
        print('Tente em 5 segundos\n')
        time.sleep(5)

def enviarMensagem2(conn): # Enviando mensagens de resposta ao cliente 2 estabelecido
    msg = input('')
    msg = '\nServidor: ' + msg
    try:
        conn.send(msg.encode('UTF-8'))
    except:
        print('\nAlgo aconteceu')
        print('Tente em 5 segundos\n')
        time.sleep(5)

 Foi transferidor para classe
def receber(conn):
    while True:
        global bandeira
        try:
            reply = conn.recv(2048)
            reply = reply.decode('UTF-8')
            if reply[0] == '1':
                print('Cliente', reply)
                print('\n')
                start_new_thread(enviarMensagem, (conn,))
            elif reply[0] == '2':
                print('Cliente', reply)
                print('\n')
                start_new_thread(enviarMensagem2, (conn,))
            else:
                lista_de_clientes.append(reply[4])
                print('\nO cliente ' + reply[4] + ' saiu.')
                bandera = True
                break
        except:
            print('\nNão pode receber resposta')
            print('Tente em 5 segundos\n')
            time.sleep(5)
 

def enviarEspecial(conn):
    global lista_de_clientes,client
    client = lista_de_clientes.pop()
    conn.send(client.encode('UTF-8'))
'''


bandeira = False

# -------- mudanças -------

class Cli:
    def __init__(self, s, ide): # Esta ouvindo o determinado endereço
        conn, addr = s.accept()
        print('\nConexão Estabelecida.\nO Cliente é:', addr[0] + ' : ' + str(addr[1]) + '\n')
        self.conn = conn
        self.addr = addr
        self.ide = ide

        enviarEspecial()
        start_new_thread(ReceberMSG)
    
    def enviarEspecial():
        conn.send("Cliente"+ ide +".".encode('UTF-8'))

    def receberMSG():
        while True:
            try:
                reply = conn.recv(2048)
                reply = reply.decode('UTF-8')
                
                start_new_thread(enviarMensagemAll, (mens))

            except:
                print('\nNão pode receber resposta')
                print('Tente em 5 segundos\n')
                time.sleep(5)

    def enviarMensagemAll(msg): # Enviando mensagens de resposta ao cliente 1 estabelecid
        try:
            while(allClientes < len(allClientes)):
                if (allClientes.ide != self.ide):
                    allClientes[i].enviarSelf(msg)
        except:
            print('\nAlgo aconteceu')
            print('Tente em 5 segundos\n')
            time.sleep(5)

    def enviarSelf(msg):
        try:
            conn.send(msg.encode('UTF-8'))
        except:
            print('\nAlgo aconteceu')
            print('Tente em 5 segundos\n')
            time.sleep(5)

global allClientes # lista com todos os clientes

def listing():
    ip, porta = endereco()
    s = criarSocket()
    testarSocket(s, ip, porta)

    ide = 1
    while(True):
        s.listen()
        print('\nAVISO: O Não escreva se o servidor não tiver qualquer mensagem para responder.')
        print('\nEsperando por clientes: ')
        novoCli = Cli(s, ide)
        allClientes.append(novoCli)
        ide += 1

# -------- mudanças -------


def main():
    global bandeira
    
    listing()

    while True:                         # Necessário para que los hilos no mueran
        if bandeira != True:            # Se um dos clientes se desconectar o servidor fica a espera desse cliente que se desconectou.
            conn3,addr3 = conectar(s)
            enviarEspecial(conn3)
            start_new_thread(receber,(conn3,))
            bandeira = False
main()
