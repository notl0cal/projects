for i in range(1, num + 1):
  if i % 3 == 0:
    print("Full")
  elif i % 5 == 0:
    print("Stack")
  elif i % 3 == 0 and i % 5 == 0:
    print("FullStack")