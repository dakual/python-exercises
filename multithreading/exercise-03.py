import threading,time

class MyThread(threading.Thread):
  def __init__(self, threadID, name, counter):
    super(MyThread,self).__init__()
    
    self.threadID = threadID
    self.name = name
    self.counter = counter

  def run(self):
    print("Starting: {}".format(self.name))

    # Get lock to synchronize threads
    threadLock.acquire()
    print_time(self.name, self.counter)
    # Free lock to release next thread
    threadLock.release()

    print("Existing : {}".format(self.name))

def print_time(name, counter):
  while counter:
    time.sleep(2)
    print("{0} : {1}".format(name, time.ctime(time.time())))
    counter -= 1


threadLock = threading.Lock()
threads = []

# Create new threads
t1 = MyThread(1, "Thread-1", 5)
t2 = MyThread(2, "Thread-2", 3)

# Start new Threads
t1.start()
t2.start()

# Add threads to thread list
threads.append(t1)
threads.append(t2)

# Wait for all threads to complete
for i in threads:
  i.join()

print("Exiting Main Thread")