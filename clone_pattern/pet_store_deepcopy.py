from copy import copy, deepcopy


class PetStore:
    """寵物店"""
    def __init__(self, name):
        self._name = name
        self._pet_list = []

    def set_name(self, name):
        self._name = name

    def show_myself(self):
        print('寵物店有以下動物:')
        for pet in self._pet_list:
            print(f'{pet}')
        print('')

    def add_pet(self, pet):
        self._pet_list.append(pet)


store = PetStore('Peter')
store.add_pet('dog coco')
store.show_myself()
# 深拷貝
store1 = deepcopy(store)
store1.add_pet('cat ricky')
store1.show_myself()
store.show_myself()
# 淺拷貝
store2 = copy(store)
store2.add_pet('lion amy')
store2.show_myself()
store.show_myself()



