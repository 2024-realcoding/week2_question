from priority_queue import PriorityQueue
def main():
  pq = PriorityQueue()

  pq.push("Task 1", 3)
  pq.push("Task 2", 1)
  pq.push("Task 3", 2)

  print(pq.pop())
  print(pq.pop())
  print(pq.pop())

if __name__ == "__main__":
  main()
