

import subprocess, signal, os, time

cmd = ['python','printer.py']

def handleSigint(signal, frame):
	print 'Signal recieved'
	#sys.exit(0)

signal.signal(signal.SIGINT, handleSigint)

process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

print '>', str(os.getpid())
data = process.communicate(input = str(os.getpid()) )[0]
print '<', data

time.sleep(2)

#signal.pause()

# process.send_signal(signal.SIGINT)

# data = process.communicate(input='Yippee')[0]
# print data
