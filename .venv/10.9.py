import itertools

n = int(input())
nmbr = []
for i in range(1, n+1):
    nmbr.append(i)

result = [seq for i in range(len(nmbr), 0, -1)
          for seq in itertools.combinations(nmbr, i)
          if sum(seq) == n]

print(len(result))

