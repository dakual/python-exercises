import socket, threading, time

threads = [] 

class ClientThread(threading.Thread):
  
  def __init__(self,clientAddress, clientsocket):
    threading.Thread.__init__(self)
    self.csocket = clientsocket
    self.client  = clientAddress
    self.active  = True

  def run(self):
    print ("New connection from: ", self.client)
    self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))

    while self.active:
      try:
        data = self.csocket.recv(2048)
        if not data:
          print('No connection, Bye 2')
          break
      except socket.error as e:
        print('No connection, Bye 1')
        break
      
      # msg = bytearray(data)
      # value = 0x7F & msg[0]
      # print(value)
      # print(format(value, '08b'))
      

      msg = data.decode('UTF-8')
      print("from client:", msg)
      self.csocket.send(bytes(msg,'UTF-8'))

    self.disconnect()
    

  def disconnect(self):
    print ("Client at ", self.client , " disconnected...")
    self.csocket.close()
    threads.remove(self)

    
def main():
  LOCALHOST = socket.gethostbyname(socket.gethostname())
  PORT      = 2002
  
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((LOCALHOST, PORT))
  print("Server started")
  print("Waiting for client request..")

  while True:
    server.listen(5)
    clientSocket, clientAddress = server.accept()

    newthread = ClientThread(clientAddress, clientSocket)
    newthread.start()
    threads.append(newthread)
    

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print("Keyboard interrupt")

    for th in threads:
      th.active = False