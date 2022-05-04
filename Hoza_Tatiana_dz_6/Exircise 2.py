my_file = []
my_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for i in f:
        my_text = i.split(sep=' ')
        remote_addr = my_text[:1]
        request_type = my_text[5:6]
        requested_resource = my_text[6:7]
        n = my_text[0]
        my_file.append((n, my_text[5].strip('"'), my_text[6]))
        if n not in my_dict:
            my_dict[n] = 1
        else:
            my_dict[n] += 1

value_0 = 0
key_0 = ''
for key, value in my_dict.items():
    if value > value_0:
        value_0 = value
        key_0 = key
print(f'IP - адрес спамера:{key_0}, количество отправленных запросов : {value_0}')
