import os

path = "/home/daghan/test"
for file in os.listdir(path):
    filepath = os.path.join(path, file)
    if os.path.isdir(filepath) and not file.startswith("."):
        for xFile in os.listdir(filepath):
            os.rename(os.path.join(filepath, xFile), os.path.join(path, xFile))
        os.removedirs(filepath)