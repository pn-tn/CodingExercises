from Process import Process
from FCFS import FCFS

# OPERATING SYSTEMS - FINAL PROJECT
# Aloysius Hasheem A Sendad
# CSCC 15 - B
#
# Process Management Simulation

print("HelloWorld")

# First Come First Served
a = Process(5, "a")
b = Process(3, "b")
c = Process(2, "c")

fcfs = FCFS()

fcfs.addProcess(a, 0)
fcfs.addProcess(b, 16)
fcfs.addProcess(c, 0)

fcfs.start()
print(fcfs.allComplete())
fcfs.printProgress()

fcfs.showReport()
fcfs.turnaroundTime()
