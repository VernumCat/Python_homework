immutable_var = tuple([10, 20, True, False, 'кортеж'])
print('immutable_var:', immutable_var)
#immutable_var [2] = False #данная операция не поддерживается, программа выдает ошибку
mutable_list = [10, 10, True, False, 'список']
mutable_list[1] = 20
print('mutable_list:', mutable_list)

