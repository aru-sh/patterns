import concurrent.futures
import time


def task(value):
    print(f"Task {value} started")
    time.sleep(2)
    print(f"Task {value} completed")
    return value


if __name__ == "__main__":
    """
    In the main block, we create a ThreadPoolExecutor with a maximum of 4 worker threads using the with statement, 
    which ensures that the thread pool is properly closed and resources are released when we're done. 
    We then submit 10 tasks to the executor using a list comprehension: futures = [executor.submit(task, i) for i in range(10)]. 
    
    Each call to executor.submit schedules the task function to be executed with the corresponding value of i and 
    returns a Future object representing the asynchronous execution of the task. 
    
    We wait for all tasks to complete using concurrent.futures.as_completed(futures), which is an iterator that yields 
    the Future objects as they complete. We collect the results of the completed tasks using another list 
    comprehension: results = [future.result() for future in concurrent.futures.as_completed(futures)].
    """

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(task, i) for i in range(0, 10)]
        results = [
            future.result() for future in concurrent.futures.as_completed(futures)
        ]

print("All tasks completed")
print(f"Results: {results}")
