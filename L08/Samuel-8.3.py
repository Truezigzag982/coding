pets_list = ['kitten', 'puppy']


def add_pet(pet):
    pets_list.append(pet)

def remove_pet(pet):
    pets_list.remove(pet)



pet = input('add pet name: ')
add_pet(pet)
print('pet list: ', pets_list)

pet = input('remove pet name: ')
remove_pet(pet)
print('pet list: ', pets_list)