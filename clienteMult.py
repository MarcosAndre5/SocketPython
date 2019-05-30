import socket
import threading
import sys
import pickle
import os

class Cliente():
	def __init__(self, host="127.0.0.1", port=4000):
		os.system('clear')
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))
		msg_recv = threading.Thread(target=self.msg_recv)
		msg_recv.daemon = True
		msg_recv.start()
		print("----- Bem Vindo ao Chat -----")
		nome = input("Digite seu nome: ")
		self.send_msg("\n" + nome + " entrou no chat.")
		while True:
			msg = input('\nVocê -> ')
			if msg != 'sair':
				msg = "\n" + nome + ": " + msg
				self.send_msg(msg)
			else:
				self.send_msg("\n" + nome + " saiu do chat.")
				self.sock.close()
				sys.exit()

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def send_msg(self, msg):
		self.sock.send(pickle.dumps(msg))

c = Cliente()