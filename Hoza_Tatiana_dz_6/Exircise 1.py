with open('nginx_logs.txt','r', encoding='utf-8') as f:

    for i in f:
        my_text = i.split(sep=' ')
        remote_addr = my_text[:1]
        request_type = my_text[5:6]
        requested_resource = my_text[6:7]
        print(f'{remote_addr}{request_type}{requested_resource}')
