import time
import asyncio

# Synchronous
def task(name):
    print(f"{name} started")

    time.sleep(2)

    print(f"{name} finished")

start = time.time()

task("Task 1")
task("Task 2")

end = time.time()
print(f"Synchronous Total Time: {end - start:.2f} seconds")

print("\n================================\n")

# Asynchronous
async def async_task(name):
    start = time.time()
    print(f"{name} started")

    await asyncio.sleep(2)

    print(f"{name} finished")

async def main():
    await asyncio.gather(
        async_task("Task 1"),
        async_task("Task 2")
    )

start = time.time()

asyncio.run(main())

end = time.time()

print(f"Asynchronous Total Time: {end - start:.2f} seconds")
