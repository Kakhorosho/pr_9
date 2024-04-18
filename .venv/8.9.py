n = int(input())
number = 0
dividers = []
count =0

while n > number + 1:
    number += 1
    a = n - number
    dividers.append(a)

for i in dividers:
    for j in dividers:
        if i**2 + j**2 == n:
            count +=1
print(count // 2)
