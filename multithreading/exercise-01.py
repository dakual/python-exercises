import threading, time


def print_time(args, delay):
  cnt = 0
  while cnt < 5:
    time.sleep(delay)
    cnt += 1
    threadName = threading.current_thread().name
    print("{0} : {1} : {2}".format(threadName, args, time.ctime(time.time())))



if __name__ == "__main__":
  # creating threads
  t1 = threading.Thread(target=print_time, name="th1", args=("args", 1))
  t2 = threading.Thread(target=print_time, name="th2", args=("args", 2))

  # starting threads
  t1.start()
  t2.start()

  # wait until all threads finish
  t1.join()
  t2.join()

  print("done")