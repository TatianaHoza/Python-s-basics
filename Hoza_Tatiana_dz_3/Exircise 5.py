import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_jokes(num):
    my_list = []
    for i in range(num):
        my_nouns = random.choice(nouns)
        my_adverbs = random.choice(adverbs)
        my_adjectives = random.choice(adjectives)
        my_list.append(f'{my_nouns} {my_adverbs} {my_adjectives}')
    return my_list
print(get_jokes(2))

