def single_root_words(root_words, *other_words):
    same_words = list()
    for i in other_words:
        low_root = root_words.lower()
        low_i = i.lower()
        if low_root.count(low_i) >= 1 or low_i.count(low_root) >= 1:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
