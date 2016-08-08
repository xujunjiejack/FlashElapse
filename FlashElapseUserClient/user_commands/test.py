from threading import Timer
import sched, time
from threading import Thread
from _thread import start_new_thread

def print_int():
	i = 0
	while i < 10:
		time.sleep(3)
		i += 1
		print("JJ")

start_new_thread(print_int,())
while True:
	continue
