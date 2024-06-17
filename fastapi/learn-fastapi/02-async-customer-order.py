import threading
import time

def cook_food(customer_name, food_item, delay):
  """
  Simulates cooking food for a customer with a delay.
  """
  print(f"Cook started preparing {food_item} for {customer_name}")
  time.sleep(delay)  # Simulates cooking time
  print(f"Cook finished preparing {food_item} for {customer_name}")
  print()

def take_order(customer_name):
  """
  Simulates taking an order from a customer.
  """
  time.sleep(1)  # Simulates order taking time
  food_item = f"{customer_name}'s order"
  print(f"Order taken from {customer_name}: {food_item}")
  return food_item

def serve_customer(customer_name):
  """
  Simulates taking an order, cooking food, and serving a customer concurrently.
  """
  order_thread = threading.Thread(target=take_order, args=(customer_name,))
  order_thread.start()

  food_item = order_thread.join()  # Wait for order to be taken
  cook_thread = threading.Thread(target=cook_food, args=(customer_name, food_item, 2))
  cook_thread.start()

  # Simulate other tasks the main thread can do concurrently with cooking
  print(f"Main thread doing other tasks for {customer_name}")
  time.sleep(1)

  cook_thread.join()  # Wait for cooking to finish
  print(f"Served {food_item} to {customer_name}")
  print()
  

if __name__ == "__main__":
 customer1 = "Alice"
 customer2 = "Bob"
 serve_customer(customer1)  # Concurrently serve customer 1
 serve_customer(customer2)  # Concurrently serve customer 2 (while serving customer 1)
