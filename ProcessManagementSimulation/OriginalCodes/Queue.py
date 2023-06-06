class Queue:

    def __init__(self):
        self.line = []


    # adds x to the queue
    def add(self, x):
        self.line.append(x)


    # removes first index
    def remove(self):
        temp = self.line.pop(0)
        return temp


    def printLine(self):
        for i in self.line:
            print(i)
