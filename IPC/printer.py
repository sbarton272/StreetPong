
from sys import stdin
import signal

# for i in xrange(1,10):
# 	print "Stuff", i

# print stdin.readline()

import os

pid = int(stdin.readline().strip())
print pid

os.kill(pid, signal.SIGINT)