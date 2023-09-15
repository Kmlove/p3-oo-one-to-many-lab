class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    def __repr__(self):
        return f"<Name: {self.name} belongs to {self.owner}>"

    def get_pet_type(self):
        return self._pet_type
    def set_pet_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception("Please enter a valid pet type")
    pet_type = property(get_pet_type, set_pet_type)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Please enter a vaild Pet object")
    
    def get_sorted_pets(self):
        pet_list = self.pets()

        def sort_func(e):
            return e.name
        pet_list.sort(key=sort_func)

        return pet_list
    
# owner = Owner("John")
# pet1 = Pet("Fido", "dog", owner)
# pet2 = Pet("Clifford", "dog", owner)
# pet3 = Pet("Whiskers", "cat", owner)
# pet4 = Pet("Jerry", "reptile", owner)

# import ipdb; ipdb.set_trace()