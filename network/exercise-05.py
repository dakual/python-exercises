#!/usr/bin/env python3

import signal
import socket
import threading


class Client_Thread:
	def __init__(self, c_socket, addr, debug=False):
		RECV_BUFSIZE = 1024
		self.debug = debug
		self.c_socket = c_socket
		self.c_socket_str = '%s:%d' % (addr[0],addr[1])
		self.c_socket.send('Welcome to the server.\n'.encode())
		self._print_debug('connected')

		# main loop: receive/send data
		while True:
			data = self.c_socket.recv(RECV_BUFSIZE)
			if not data:
				break
			self._do_stuff(data)
		self.c_socket.close()
		self._print_debug('disconnected')


	# play with received data
	def _do_stuff(self, data):
		reply = ('OK: %s' % data.decode()).encode()
		self.c_socket.sendall(reply)


	def _print(self, s):
		print('[Client] %s> %s' % (self.c_socket_str, s))


	def _print_debug(self, s):
		if self.debug: self._print(s)



class Socket_Server:
	def __init__(self, host='', port=1234, debug=False):
		self.host = ''
		self.port = port
		self.debug = debug
		listen_backlog = 10

		# create socket
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._print_debug('Socket created')

		# bind socket to address
		try:
			self.socket.bind((self.host, self.port))
			self._print_debug('Socket bind complete')
		except socket.error as msg:
			self._print('Bind failed: %s' % (msg))
			exit(1)

		# accept connections
		self.socket.listen(listen_backlog)  # listen_backlog optional in >= v3.5
		self._print('Socket now listening on port %d' % self.port)

		# set signal handler
		signal.signal(signal.SIGINT, self._shutdown_handler)   # KeyboardInterrupt
		signal.signal(signal.SIGTERM, self._shutdown_handler)  # kill

		# main loop to accept connections
		while 1:
			try:
				c_socket, addr = self.socket.accept()
			except (KeyboardInterrupt, InterruptedError):
				break

			thread = threading.Thread(target=Client_Thread, args=(c_socket, addr, self.debug))
			thread.setDaemon(True)
			thread.start()

			self._print_debug('Active clients: %d' % self.get_active_client_connections())

	# return number of thread without main thread ^= connections
	def get_active_client_connections(self):
		return threading.active_count() - 1

	# close socket on shutdown
	def shutdown(self):
		self.socket.close()
		self._print('Gracefull shutdown. Bye.')

	def _shutdown_handler(self, signum, frame):
		self.shutdown()

	def _print(self, s):
		print('[SERVER] %s' % s)

	def _print_debug(self, s):
		if self.debug: self._print(s)


if __name__ == "__main__":
	server = Socket_Server(debug=True)