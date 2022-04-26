from itertools import islice

n = int(input('n = '))
odd_to_n = (i for i in range(1, (n+1), 2))
print(*islice(odd_to_n, n))
