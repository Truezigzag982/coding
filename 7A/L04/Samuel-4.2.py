dict_aminals = {
    "aligator": "短吻鳄🐊",
    "girraffe": "长颈鹿🦒",
    "deer": "鹿🦌",
    "jaguar": "美洲豹🐆"
   }
sorted_key = sorted(dict_aminals)
print('sorted keys: ', sorted_key)

d_ascending = {}
for k in sorted_key:
    d_ascending[k] = dict_aminals[k]
print("ascending dict: ", d_ascending)

sorted_key = sorted(dict_aminals, reverse=True)
print('sorted keys: ', sorted_key)
d_descending = {k: dict_aminals[k] for k in sorted_key}
print('descending dict: ', d_descending)

animal = input('Please type animal name to search: ')
if animal in dict_aminals:
    print(f'{animal}:{dict_aminals[animal]}')
else:
    print(f'sorry, {animal} is not found in the dictionary.:(')