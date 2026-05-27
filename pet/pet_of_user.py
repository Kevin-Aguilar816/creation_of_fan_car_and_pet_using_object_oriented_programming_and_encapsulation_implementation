from pet_class import Pet


def set_pet_name(Pet, name):
    pet = Pet(name)
    return pet


if __name__ == "__main__":
    name = input("Enter your pet's name:")
    pet = set_pet_name(Pet, name)
