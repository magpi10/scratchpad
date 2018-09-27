import time
from random import randint
array = []
for i in range(0,10):
  chose = randint(1,10)
  array.append(chose)
  chose = randint(1,10)
  array.append(chose)
  time.sleep(1)
  print(array)
  time.sleep(1)
print('There you go. Theres your random numbers')
print(array)
  