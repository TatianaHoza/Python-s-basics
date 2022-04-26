def thesaurus(*args):
    my_dictionary = dict()
    for name in args:
        my_dictionary.setdefault(name[0], [])
        my_dictionary[name[0]].append(name)
    return my_dictionary
print(thesaurus("Иван", "Мария", "Петр", "Илья"))
