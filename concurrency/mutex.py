import threading
import time

counter = 0

mutex = threading.Lock()


def increment_counter():
    global counter

    mutex.acquire()
    try:
        counter += 1
        print(f"Counter value: {counter}")
        time.sleep(2)
    finally:
        mutex.release()


if __name__ == "__main__":
    """
    A mutex is a synchronization primitive that ensures only one thread can access a shared resource at a time. 
    This is useful when you have a critical section of code that modifies shared data or performs operations 
    that cannot be interrupted or executed concurrently.
    
    In this example, we have a shared counter variable and two threads that increment the counter. 
    We use a threading.Lock object as a mutex to ensure that only one thread can access the critical section 
    (where the counter is incremented) at a time.
    
    When a thread acquires the lock using mutex.acquire(), it enters the critical section. 
    If another thread tries to acquire the lock while it's held by another thread, it will block until the lock is 
    released by the owning thread using mutex.release().
    """

    thread1 = threading.Thread(target=increment_counter)
    thread2 = threading.Thread(target=increment_counter)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
