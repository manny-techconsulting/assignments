import os
def getfileName(filename):
    file = os.path.join(os.path.dirname(__file__), filename)
    print(file)
    return file
