import asyncio
import random
import time


async def worker(n, delay):
    """Simulate a long-running task"""

    print(f"Starting worker {n}")
    await asyncio.sleep(delay)
    print(f"Worker {n} finished!")
    return n


async def main():
    tasks = []
    for n in range(5):
        delay = random.uniform(1, 3)
        task = asyncio.create_task(worker(n, delay))
        tasks.append(task)

    results = await asyncio.gather(*tasks, return_exceptions=True)
    print("Results:", results)


if __name__ == "__main__":
    """
    The main coroutine is the entry point for the program. It creates five tasks by calling the worker coroutine with 
    different task numbers (n) and random delays.
    
    The tasks are created using asyncio.create_task and stored in a list (tasks).
    
    The asyncio.gather function is used to run all the tasks concurrently and wait for them to complete. 
    The return_exceptions=True argument ensures that any exceptions raised by the tasks are propagated to the results list.
    
    After all tasks have completed, the results list contains the return values (task numbers) from each task.
    """
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")
