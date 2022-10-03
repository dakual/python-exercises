"""
with open("test.txt","w") as file:
    file.write("Hello World\n") 
    file.write("This is our new text file\n") 
    file.write("and this is another line.\n") 
    file.write("Why? Because we can.\n") 
"""

with open("test.txt") as fromFile:
    with open("test2.txt","w") as toFile:
        readByte = fromFile.read(1024)
        while len(readByte) > 0:
            toFile.write(readByte)
            readByte = fromFile.read(1024)
