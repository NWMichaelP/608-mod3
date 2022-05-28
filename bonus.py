import random
import statistics

data = [random.randrange(500) for x in range(0,500)]

print(round(statistics.pvariance(data),2))
print(round(statistics.pstdev(data),2))