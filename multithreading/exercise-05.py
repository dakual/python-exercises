import threading
import time
import logging
import random
from queue import Queue

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)s) %(message)s',)


class ProducerThread(threading.Thread):
  def __init__(self, target=None, name=None):
    super(ProducerThread,self).__init__()
    self.target = target
    self.name = name

  def run(self):
    while True:
      if not queue.full():
        item = random.randint(1,10)
        queue.put(item)
        logging.debug('Putting ' + str(item) + ' : ' + str(queue.qsize()) + ' items in queue')
        time.sleep(random.random())
    return

class ConsumerThread(threading.Thread):
  def __init__(self, target=None, name=None):
    super(ConsumerThread,self).__init__()
    self.target = target
    self.name = name
    return

  def run(self):
    while True:
      if not queue.empty():
        item = queue.get()
        logging.debug('Getting ' + str(item) + ' : ' + str(queue.qsize()) + ' items in queue')
        time.sleep(random.random())
    return

if __name__ == '__main__':
  # create the shared queue
  queue = Queue(10)

  # start the producer
  producer = ProducerThread(name='producer')
  producer.start()

  time.sleep(2)

  # start the consumer
  consumer = ConsumerThread(name='consumer')
  consumer.start()
