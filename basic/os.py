import os

path = "/home/daghan/test"
for file in os.listdir(path):
    dosya = os.path.join(path, file)
    if os.path.isfile(dosya):
        ext = file.split(".")[-1]
        extdir = os.path.join(path, ext)
        if not os.path.isdir(extdir):
            os.mkdir(extdir)
        os.rename(dosya, os.path.join(extdir, file))