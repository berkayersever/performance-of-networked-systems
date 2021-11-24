import math
def blocking_probability():
  print((1 / math.factorial(5)) / (sum(1 / math.factorial(i) for i in range(0, 6))))

blocking_probability()