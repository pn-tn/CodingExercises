class Process:

    # length - length of process
    # completed - how much of the process is completed
    def __init__(self, x, n):
        self.length = x
        self.completed = 0
        self.name = n
        self.completionTime = None
        self.arrivalTime = None
