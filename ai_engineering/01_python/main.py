import threading
import time


def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")


thread1 = threading.Thread(target=task, args=("Task 1",))
thread2 = threading.Thread(target=task, args=("Task 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All tasks finished")
