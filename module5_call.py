from module5_mod import NumberProcessor
def main():
  processor = NumberProcessor()
  While True:
  try:
    n = int(imput("Enter a positive integer N:"))
    if n<= 0:
      print("N must be positive.")
      continue
    break
  except ValueError:
    print("Please enter a valid integer.")
  for i in range(n):
    while True:
      try:
        num = int(input(f"Enter number {i+1}:"))
        processor.insert_number(num)
        break
      except ValueError:
        print("Please enter a valid integer.")
      while True:
        try:
          x = int(input("Enter the number X to search for: "))
        break
      except ValueError:
         print("Please enter a valid integer.")
      index = processor.search_number(x)
      print(index)

if__name__ == "__main__":
main()
