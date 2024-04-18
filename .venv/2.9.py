import math

n = int(input())
if n > 2:
     while n > 2:
        n = math.sqrt(n)
        print(f'{n:.3f}')
