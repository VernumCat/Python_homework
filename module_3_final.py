# def calculate_structure_sum(data):
#     summa = float()
#     for elem in data:
#         if isinstance(elem, (list, tuple, set)):
#             summa += calculate_structure_sum(elem)
#         if isinstance(elem, dict):
#             summa += calculate_structure_sum(list(elem.items()))
#         if isinstance(elem, (int, float)):
#             summa += elem
#         if isinstance(elem, str):
#             summa += int(len(elem))
#     return round(summa, 2)

def calculate_structure_sum(data):
    summa = float()
    if not data:
        return 0

    elif isinstance(data, (list, tuple)):
        return summa + calculate_structure_sum(data[0]) + calculate_structure_sum(data[1:])
    elif isinstance(data, set):
        return calculate_structure_sum(list(data))
    elif isinstance(data, dict):
        return summa + calculate_structure_sum(list(data.items()))
    elif isinstance(data, (int, float)):
        return summa + data
    elif isinstance(data, str):
        return summa + int(len(data))


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
