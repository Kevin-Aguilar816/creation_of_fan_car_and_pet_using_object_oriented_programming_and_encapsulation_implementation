from fan_class import Fan
from car_class import Car
from pet_class import Pet


def get_pet():
    pet = Pet()
    pet.set_name(input("Enter your pet's name: "))
    pet.set_animal_type(input("Enter your pet's animal type: "))
    pet.set_age(float(input("Enter your pet's age: "))
    return pet
