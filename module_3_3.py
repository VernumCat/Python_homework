def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [111, 2.5, 'peace']
values_dict = {'a': 0.5, 'b': 1, 'c': 'code'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [999, '9!9']
print_params(*values_list_2, 42)
