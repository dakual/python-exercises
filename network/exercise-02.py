import imp


import socket, subprocess, sys
from datetime import datetime

subprocess.call("clear", shell=True)

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

started = datetime.now()

print ("_" * 60)
print("Scanning Target: " + remoteServerIP)
print("Scanning started at: " + str(started))
print ("_" * 60)



try:
  for port in range(1,6000):
    sock   = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = sock.connect_ex((remoteServerIP, port))
    
    if result == 0:
      print("Port {}: Open".format(port))
    
    sock.close()
except KeyboardInterrupt:
  print("You pressed Ctrl+C")
  sys.exit()

except socket.gaierror:
  print("Hostname could not be resolved. Exiting")
  sys.exit()

except socket.error:
  print("Couldn't connect to server")
  sys.exit()


print('Scanning Completed in in ', datetime.now() - started)