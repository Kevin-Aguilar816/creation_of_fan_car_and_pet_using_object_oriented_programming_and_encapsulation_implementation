from pet_class import Pet


def pet_of_user():
    pet = Pet()
    pet.set_name(input("Enter your pet's name: "))
    pet.set_animal_type(input("Enter your pet's animal type: "))
    pet.set_age(float(input("Enter your pet's age: ")))
    return pet


if __name__ == "__main__":
    pet = pet_of_user()
    print(
        f"Your pet's name is {pet.get_name()}, it is a {pet.get_animal_type()}, and it is {pet.get_age()} years old.")
