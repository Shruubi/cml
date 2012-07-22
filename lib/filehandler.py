class FileHandler:
    def __init__(self, filename, ioSelect):
        self.FILE = open(filename, ioSelect)

    def cleanup(self):
        self.FILE.close()

    def fetchList(self):
        returner = self.FILE.readlines()
        #cleanup the newlines at the end
        for i in range(len(returner)):
            returner[i] = returner[i].strip()
        return returner

    def getFile(self):
        return self.FILE




