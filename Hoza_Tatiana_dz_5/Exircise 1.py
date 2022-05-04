n = int(input('n = '))
def odd_nums(n):
   for i in range(1, n+1, 2):
      yield i
odd_to_n = odd_nums(n)
print(type(odd_to_n))
print(odd_to_n)


