from pet_class import Pet


def set_pet_name(Pet, name):
    pet = Pet(name)
    return pet


def set_pet_animal_type(Pet, animal_type):
    pet = Pet(animal_type)
    return pet


if __name__ == "__main__":
    name = input("Enter your pet's name: ")
    animal_type = input("Enter your pet's animal type: ")
