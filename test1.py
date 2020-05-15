import time
from queue import Queue
from control_loop import ControlLoop

cqi = Queue()
cqo = Queue()

uri = "http://192.168.10.237:52261/"

c = ControlLoop(uri, cqi, cqo)

c.start()

time.sleep(2)
cqi.put(['play', []])

while True:
	print(cqo.get())

c.join()
