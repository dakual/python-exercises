import threading, time

class MyThread(threading.Thread):
  def __init__(self, threadId, name, counter):
    threading.Thread.__init__(self)
    self.threadId = threadId
    self.name = name
    self.counter = counter

  def run(self):
    print("Starting {}".format(self.name))
    print_time(self.name, self.counter, 2)
    print("Exiting {}".format(self.name))


def print_time(name, counter, delay):
  while counter:
    time.sleep(delay)
    print("{0} : {1}".format(name, time.ctime(time.time())))
    counter -= 1


t1 = MyThread(1, "Thread-1", 3)
t2 = MyThread(1, "Thread-2", 5)
t1.start()
t2.start()

print("Exiting Main Thread")