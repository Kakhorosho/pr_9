n = int(input('Введите количество упаковок: '))
numbers = []
k = n - 1
while k > 0:
    if n % k == 0:
        numbers.append(k)
        k -= 1
    k -= 1

while n // max(numbers) <= 2:
    numbers.remove(max(numbers))
    print(f'Максимальное число упаковок эскимо: {n} // {max(numbers)} = {n // max(numbers)}')


