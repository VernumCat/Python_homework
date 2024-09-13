# работа со словарем
my_dict = {'Oksana': 1994, 'Igor': 2004, 'Klara': 2024}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Oksana'))
print('Not existing value:', my_dict.get('Alex'))
my_dict.update({'Eva': 2000, 'Egor': 2001})
print('Deleted value:', my_dict.pop('Klara'))
print('Modified dictionary:', my_dict)
# работа с множеством
print('')
my_set = {1, 2, 3, 1, 2, 3, 'fool'}
print('Set:', my_set)
my_set.add(3.14)
my_set.add(5.15)
my_set.discard(3)
print('Modified set:', my_set)