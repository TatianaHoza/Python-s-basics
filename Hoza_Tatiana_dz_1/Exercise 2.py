my_list = []
for i in range(1, 1001, 2):
    my_list.append(i ** 3)
print(my_list)
sum_i = 0
for i in my_list:
    origin_val = i
    sum_p = 0
    while i > 0:
        sum_p += i % 10
        i = i // 10
    if sum_p % 7 == 0:
        sum_i += origin_val
print(sum_i)
sum_i = 0
for i in my_list:
    i += 17
    origin_val = i
    sum_p = 0
    while i > 0:
        sum_p += i % 10
        i = i // 10
    if sum_p % 7 == 0:
        sum_i += origin_val
print(sum_i)