import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
  try:
    c, addr = s.accept()
    print('Got connection from', addr)

    c.send('Thank you for connecting'.encode())
  except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    break
  
  c.close()