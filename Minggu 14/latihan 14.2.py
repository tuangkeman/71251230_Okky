

print(' 1. List menjadi Set ')
data_list = [1, 2, 3, 2, 4, 1, 5]
print(f'Sebelum (List) : {data_list}')
data_set = set(data_list)
print(f'Sesudah (Set)  : {data_set}')

print('\n 2. Set menjadi List ')
data_set2 = {10, 20, 30, 40, 50}
print(f'Sebelum (Set)  : {data_set2}')
data_list2 = list(data_set2)
print(f'Sesudah (List) : {data_list2}')

print('\n 3. Tuple menjadi Set ')
data_tuple = (7, 7, 8, 9, 9, 10)
print(f'Sebelum (Tuple): {data_tuple}')
data_set3 = set(data_tuple)
print(f'Sesudah (Set)  : {data_set3}')

print('\n 4. Set menjadi Tuple ')
data_set4 = {'apel', 'mangga', 'jeruk', 'pisang'}
print(f'Sebelum (Set)  : {data_set4}')
data_tuple2 = tuple(data_set4)
print(f'Sesudah (Tuple): {data_tuple2}')
