import os


for i in range(1, 11):
  with open(f"test{i}.txt", "w") as fo:
    print(i, file=fo)

os.system("touch out.log && mkdir newdir && cd newdir && touch in.log && touch in.txt")
