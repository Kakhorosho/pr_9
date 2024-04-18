numbers = []
dividers_of_all_robes = []

while True:
    n = int(input('Введите кол-во верёвок в сети: '))
    
    if n > 0:
        numbers.append(n)
    else:
        if n != 0:
            print('Такой верёвки не может быть')
            break
        break

for i in range(len(numbers)):
    dividers = []
    k = 2

    while k <= numbers[i]:
          if numbers[i] % k == 0:
              dividers.append(k)
          k += 1
    dividers_of_all_robes.append(dividers)

counter = []
for i in range(len(dividers_of_all_robes)):
    count = 0
    for j in range(len(dividers_of_all_robes)):
        if i != j:
            common_element = any(element in dividers_of_all_robes[j] for element in dividers_of_all_robes[i])
            if common_element:
                count += 1
    counter.append(count)

count_1 = 0
for i in range(len(counter)):
    if counter[i] == 3:
        count_1 += 1

print(count_1)




