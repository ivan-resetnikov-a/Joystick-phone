import socket as network

from json import dumps, loads, decoder

import core.const as const



class Server:
	def __init__(self):
		self.name = network.gethostname()
		self.ip   = network.gethostbyname(self.name)

		self.address = (self.ip, const.PORT)


	def start(self):
		with network.socket(network.AF_INET, network.SOCK_STREAM) as server:
			print(f'[i] Binding {self.name} at {self.address}')
			server.bind(self.address)

			print('[i] Listening for client')
			server.listen()

			while True :
				client, address = server.accept()
				self.hanleUser(client, address)


	def hanleUser(self, client, address):
		print('.' * 50)
		print(f'[+] User at {address} connected')

		name = client.recv(const.BUFFER_SIZE)
		name = name.decode()

		print(f'[?] User authorized as {name}')

		client.send(self.name.encode())

		try:
			connected = True
			while connected:
				data = client.recv(const.BUFFER_SIZE)
				data = loads(data.decode())

				if data == '!DICONNECT!' : connected = False

				print(f'[u] {name}: {data}')

				print(f'[s] {self.name}: 0')

				client.send('0'.encode())

		except decoder.JSONDecodeError:
			print('[!] User forcibly stopped connection')

		print(f'[-] User {name} at {address} disconnected')


Server().start()