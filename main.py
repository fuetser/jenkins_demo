for i in range(1, 11):
  with open(f"test{i}.txt", "w") as fo:
    print(i, file=fo)
