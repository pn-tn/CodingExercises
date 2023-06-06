from Process import Process
from RouRob import RouRob

# OPERATING SYSTEMS - FINAL PROJECT
# Aloysius Hasheem A Sendad
# CSCC 15 - B
#
# Process Management Simulation

print("HelloWorld")

# Round Robin
a = Process(9, "a")
b = Process(8, "b")
c = Process(12, "c")

rr = RouRob(2)

rr.addProcess(a, 6)
rr.addProcess(b, 5)
rr.addProcess(c, 0)

rr.start()
print(rr.allComplete())
rr.printProgress()

rr.showReport()
rr.turnaroundTime()
