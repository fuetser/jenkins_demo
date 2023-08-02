import time
import random
import os

def consume_cpu():
    # Perform some CPU-intensive operation
    for _ in range(random.randint(5000, 5000000)):
        random.random()

def consume_memory():
    # Allocate memory and hold it for some time
    # memory_hog = ['Hog'] * (100 * 1024 * 1024)  # Allocating 100 MB
    # time.sleep(5)  # Hold memory for 5 seconds
    # del memory_hog
    memory_hog = []
    for i in range(10**6):
        memory_hog.extend(["hog"] * 100)
    time.sleep(5)
    for i in range(10**6):
        memory_hog.pop()

def main():
    index = 1
    while True:
        consume_cpu()
        consume_memory()
        with open(f"text{index}.txt", "w") as fo:
            for i in range(10**5):
                fo.write("Hello, world!")
        if index % 15 == 0:
            os.system("rm *.txt")
        index += 1
        time.sleep(2)

if __name__ == "__main__":
    main()
