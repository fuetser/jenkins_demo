import os


os.mkdir("artifacts")
os.mkdir("logs")

os.chdir("artifacts")
for i in range(1, 6):
  with open(f"test{i}.txt", "w") as fo:
    print(i, file=fo)

os.mkdir("inner")
os.chdir("inner")
for i in range(6, 11):
  with open(f"test{i}.txt", "w") as fo:
    print(i, file=fo)

os.chdir("..")
os.chdir("..")
os.chdir("logs")

for i in range(1, 6):
  with open(f"log{i}.log", "w") as fo:
    print(i, file=fo)

os.mkdir("inner")
os.chdir("inner")
for i in range(6, 11):
  with open(f"log{i}.log", "w") as fo:
    print(i, file=fo)
