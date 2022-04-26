num = str(input('введите число на английском от 0 до 10: '))
num_dictionary = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
                 'ten': 'десять'}
def num_translate_adv(word):
    if word[0] == word[0].upper():
        word = word.lower()
        return num_dictionary[word].capitalize()
    else:
        return num_dictionary.get(word)
print(num_translate_adv(num))