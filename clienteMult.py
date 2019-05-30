import socket
import threading
import sys
import pickle

class Cliente():
	def __init__(self, host="localhost", port=4000):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target=self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()

		print("----- Bem vindo ao Chat -----")
		nome = input("Digite seu nome: ")

		self.send_msg(nome +" entrou no chat.")

		while True:
			msg = input('->')
			if msg != 'sair':
				msg = nome +": "+ msg
				self.send_msg(msg)
			else:
				self.send_msg(nome +" saio do chat.")
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
		