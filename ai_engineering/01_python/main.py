import threading
import time

event = threading.Event()


def worker():
    print("Worker: Waiting for signal...")
    event.wait()
    print("Worker: Signal received!")


def controller():
    time.sleep(2)
    print("Controller: Sending signal...")
    event.set()


thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=controller)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
