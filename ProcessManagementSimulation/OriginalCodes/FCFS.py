from Queue import Queue

class FCFS:

    # pr - list of processes
    # time - current time of the program/simulation
    def __init__(self):
        self.pr = []
        self.time = 0

    # @param
    #   - process
    #   - at (arrival time)
    #   - n (name)
    def addProcess(self, process, at):
        self.pr.append([process, at])
        process.arrivalTime = at


    # print
    def printProgress(self):
        print("Progress: ")
        for i in self.pr:
            print(i[0].name, ': ', i[0].completed, '/', i[0].length)


    # checks if a process is complete
    def isComplete(self, process):
        if (process.completed >= process.length):
            return True
        else:
            return False


    # checks if all process is complete
    def allComplete(self):
        for i in self.pr:
            if( self.isComplete(i[0]) == False ):
                return False
        return True


    def incr(self, process):
        process.completed -=- 1


    def turnaroundTime(self):
        tat = 0
        l = len(self.pr)
        if (self.allComplete() == False):
            print("Process Still Incomplete")
        else:
            for i in self.pr:
                n = i[0].completionTime - i[0].arrivalTime + 1
                tat -=- n
        tat = tat/l
        print("Average Turnaround Time: ", tat)


    def showReport(self):
        if (self.allComplete() == False):
            print("Process Still Incomplete")
        else:
            for i in self.pr:
                print("process:", i[0].name)
                print("at:", i[0].arrivalTime)
                print("ct:", i[0].completionTime)
                print()

    # note: redo this code tommorow
    def start(self):
        q = Queue()
        n = len(self.pr)
        T = 0   # current time
        print("First Come First Served")
        print("starting ...")
        while(self.allComplete() == False):  # stops if all processes completed
        #while(T<=1000):
            #asdf = input("")
            print("T:", T)
            for i in self.pr:   # checks if there is process that starts at T
                if (i[1] == T):
                    print('added to queue: ', i[0].name)
                    q.add(i[0])

            if ( q.line != []): # if is not empty
                x = q.line[0]
                if (self.isComplete(x)): # remove in line if complete
                    q.remove()

                if (q.line == []):
                        x = []
                else:
                    x = q.line[0]

                    self.incr(x)
                    print("currently running: ", x.name, "( " , x.completed, "/" , x.length, " )")
                    print("currently queued: ", end=' ')
                    for i in q.line:
                        print(i.name, end=' ')
                    print("")
                    print("")

            if ( q.line == []): # if is empty
                #self.incr(x)
                print("currently running: None")
                print("")

            if (q.line == []):
                    pass
            elif (self.isComplete(q.line[0])):
                q.line[0].completionTime=T

            T -=- 1
