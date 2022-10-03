import threading, time
from queue import Queue


class MyThread(threading.Thread):
  def __init__(self, name, workQueue):
    super(MyThread,self).__init__()
    self.name = name
    self.workQueue = workQueue

  def run(self):
    print("Starting: {}".format(self.name))

    while not exitFlag:
      queueLock.acquire()
      if not self.workQueue.empty():
        data = self.workQueue.get()
        print("{0} processing {1}".format(self.name, data))
      
      queueLock.release()
      time.sleep(1)
    
    print("Existing : {}".format(self.name))

exitFlag  = 0
nameList  = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
workQueue = Queue(10)
queueLock = threading.Lock()
threads   = []

# Create new threads
t1 = MyThread("Thread-1", workQueue)
t2 = MyThread("Thread-2", workQueue)

# Start new Threads
t1.start()
t2.start()


# Add threads to thread list
threads.append(t1)
threads.append(t2)


# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1


# Wait for all threads to complete
for i in threads:
  i.join()

print("Exiting Main Thread")