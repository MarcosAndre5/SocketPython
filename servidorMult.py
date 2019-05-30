import socket
import threading
import sys
import pickle
import os

class Servidor():
	def __init__(self, host="127.0.0.1", port=4000):
		os.system('clear')
		self.clientes = [] # Array para clientes
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #
		self.sock.bind((str(host), int(port)))
		self.sock.listen(10)
		self.sock.setblocking(False)
		aceptar = threading.Thread(target=self.aceptarCon)
		procesar = threading.Thread(target=self.procesarCon)
		aceptar.daemon = True
		aceptar.start()
		procesar.daemon = True
		procesar.start()
		print("----- Servidor da Aplicação -----\n")
		while True:
			msg = input('Servidor -> ')
			if msg == 'sair':
				self.sock.close()
				sys.exit()
			else:
				pass

	def msg_to_all(self, msg, cliente, id):
		for c in self.clientes:
			try:
				if c != cliente:
					c.send(msg)
			except:
				self.clientes.remove(c)

	def aceptarCon(self):
		while True:
			try:
				conn, addr = self.sock.accept()
				conn.setblocking(False)
				self.clientes.append(conn)
			except:
				pass

	def procesarCon(self):
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(1024)
						if data:
							self.msg_to_all(data, c, id)
					except:
						pass

s = Servidor()