import threading
import time

semaphore = threading.Semaphore(2)


def worker(name):
    semaphore.acquire()

    try:
        print(f"{name} is working...")
        time.sleep(2)
    finally:
        semaphore.release()
        print(f"{name} is done working.")


if __name__ == "__main__":
    """
    A semaphore is a synchronization primitive that controls access to a shared resource with a limited number of instances. 
    It's like a mutex, but it allows multiple threads to access the shared resource up to a specified limit.
    
    In this example, we create a threading.Semaphore object with a limit of 2, which means that at most 2 threads  can 
    acquire the semaphore at any given time.
    
    When a thread calls semaphore.acquire(), it tries to acquire the semaphore. If the current number of acquired 
    semaphores is less than the limit, the thread proceeds. If the limit has been reached, the thread blocks until 
    another thread releases the semaphore using semaphore.release().
    
    In the worker function, we simulate some work by printing a message and sleeping for 2 seconds.
    The semaphore ensures that only two threads can execute this critical section simultaneously.
    """
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(f"Thread {i}",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
