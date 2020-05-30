import time
from functools import wraps
def tempo(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    t1 = time.time()
    result = func(*args, **kwargs)
    t2 = time.time()
    print(func.__name__, t2 - t1)
    return result
  return wrapper

@tempo
def contador(n):
  while n > 0: n -= 1

contador(1000000)
contador(10000000)
