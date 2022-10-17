import socket, threading


def main():   
  host = socket.gethostbyname(socket.gethostname())
  port = 2002

  server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server.connect((host,port))

  def ping():
    server.send(b'\x10')
    threading.Timer(3.0, ping).start()

  #ping()

  message = "Hello, World!"
  while True:
    #server.send(message.encode())
    data = server.recv(2048)

    print('Received message from the server :',str(data.decode('UTF-8')))

    cont = input('\Type your message:')
    server.send(cont.encode('UTF-8'))

  server.close()



if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print("Keyboard interrupt")