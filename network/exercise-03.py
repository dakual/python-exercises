import subprocess

address = "127.0.0.1"
result  = subprocess.call(["ping", "-c", "1", address])

if result == 0:
    print( "ping to", address, "OK")
elif result == 2:
    print("no response from", address)
else:
    print("ping to", address, "failed!")

