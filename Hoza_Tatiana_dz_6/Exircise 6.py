import json
with open('bakery.csv', 'w', encoding='utf-8') as f:
    f.writelines('\npython add_sale.py 5978,5\npython add_sale.py 8914,3\npython add_sale.py 7879,1\n'
                 'python add_sale.py 1573,7\npython show_sales.py')
with open('bakery.csv', 'r', encoding='utf-8') as f:
    my_text = f.read().split('\n')
print(my_text)
with open('bakery.csv', 'r', encoding='utf-8') as f:
    f.seek(1)
    print(f.read())
with open('bakery.csv', 'r', encoding='utf-8') as f:
    text = f.readlines()
    print(text[3])
with open('bakery.csv', 'r', encoding='utf-8') as f:
    my_text = f.read().split('\n')
    my_str = json.dumps(my_text)
    print(my_str)
    print(my_str.find(',5'))
with open('bakery.csv', 'r', encoding='utf-8') as f:
    f.seek(29)
    print(f.readline())


