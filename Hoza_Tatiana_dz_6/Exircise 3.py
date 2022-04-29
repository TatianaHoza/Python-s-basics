from itertools import zip_longest
with open('users.csv', 'w', encoding='utf-8') as my_file_users:
    my_file_users.writelines('Иванов,Иван,Иванович\nПетров,Петр,Петрович\nВикторов, Виктор, Викторович')
with open('users.csv', 'r', encoding='utf-8') as my_file_users:
    users = my_file_users.read().split('\n')
print(users)

with open('hobby.csv', 'w', encoding='utf-8') as my_file_hobby:
    my_file_hobby.writelines('скалолазание,охота\nгорные лыжи')
with open('hobby.csv', 'r', encoding='utf-8') as my_file_hobby:
    hobby = my_file_hobby.read().split('\n')
print(hobby)

my_diction = dict(zip_longest(users, hobby, fillvalue=None))
print(my_diction)

