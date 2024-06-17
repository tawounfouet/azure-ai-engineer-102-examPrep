import asyncio

async def wait_and_print(message: str, delay: int):
  """
  This async function waits for a specified delay and then prints a message.
  """
  await asyncio.sleep(delay)  # Simulates asynchronous waiting
  print(message)

async def main():
  """
  This async function defines the tasks and runs them concurrently.
  """
  # Define two tasks with different messages and delays
  task1 = asyncio.create_task(wait_and_print("Hello from task 1!", 2))
  task2 = asyncio.create_task(wait_and_print("Hello from task 2!", 1))

  # Run the tasks concurrently using asyncio.gather
  await asyncio.gather(task1, task2)  # Wait for both tasks to finish

if __name__ == "__main__":
  # Run the main coroutine
    asyncio.run(main())