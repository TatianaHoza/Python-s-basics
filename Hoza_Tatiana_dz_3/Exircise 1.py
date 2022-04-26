num = str(input('введите число на английском от 0 до 10: '))
num_dictionary = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
                 'ten': 'десять'}
def num_translate(word):
    if word in num_dictionary:
        return num_dictionary[word]
    else:
        print('None')
print(num_translate(num))







