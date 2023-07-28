import time


data = []
with open("/dev/urandom", "rb") as fi:
  chunck = fi.read(1024)
  data.append(chunck)
  time.sleep(0.5)
