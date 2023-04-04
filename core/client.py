import socket as network
import threading
import time

from json import dumps, loads

import core.const as const




class Client:
	def __init__(self):
		self.name = network.gethostname()

		self.address = ('192.168.192.202', const.PORT)


	def disconnect(self):
		self.client.close()


	def connect(self):
		# Network protocol
		self.connected = True
		self.client = network.socket(network.AF_INET, network.SOCK_STREAM)

		# Connecting
		print(f'[+] Connecting {self.name} to {self.address}')
		self.client.connect(self.address)

		# Authorizing
		self.client.send(self.name.encode())

		data = self.client.recv(const.BUFFER_SIZE)
		self.server = data.decode()


	def send(self, data):
		if data == '!DICONNECT!': self.connected = False

		print(f'[c] {self.name}: {data}')
		
		self.client.send(dumps(data).encode())

		data = self.client.recv(const.BUFFER_SIZE)
		data = data.decode()
		
		print(f'[s] {self.server}: {data}')