import socket

Host = '127.0.0.1'
Port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((Host, Port))
	s.listen()
	conn, addr = s.accept()
	with conn:
			print('Server is connected with address', addr)
			while True:
						data = conn.recv(2048)
						if not data:
							break
						conn.sendall(data)