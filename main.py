import time
import random

def consume_cpu():
    # Perform some CPU-intensive operation
    for _ in range(1000000):
        random.random()

def consume_memory():
    # Allocate memory and hold it for some time
    memory_hog = ['Hog'] * (100 * 1024 * 1024)  # Allocating 100 MB
    time.sleep(5)  # Hold memory for 5 seconds
    del memory_hog

def main():
    while True:
        consume_cpu()
        consume_memory()
        time.sleep(2)

if __name__ == "__main__":
    main()
