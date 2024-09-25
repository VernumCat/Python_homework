calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return tuple([len(string), string.upper(), string.lower()])

def is_contains(string, list_to_seach):
    count_calls()
    for i in range(0,len(list_to_seach)):
        i2 = list_to_seach[i]
        list_to_seach[i] = i2.lower()
    return string.lower() in list_to_seach

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
