from fan_class import Fan
from car_class import Car
from pet_class import Pet


def get_pet():
    pet = Pet()
    pet.set_name(input("Enter your pet's name: "))
    pet.set_animal_type(input("Enter your pet's animal type: "))
    pet.set_age(float(input("Enter your pet's age: "))
    return pet

def car_accelerate(car, fan_one, pet):
    while car.get_speed() != "25 km/h":
        car.accelerate()
        print(
            f"My {my_car.get_year_model()} {my_car.get_make()} has a speed of ({car.get_speed()} km/h)")

    fan_one.set_is_on(True)
    print(f"{pet.get_name()} is enjoying the fan at {fan_one.get_speed()} speed while my {my_car.get_year_model()} {my_car.get_make()} is accelerating!")
