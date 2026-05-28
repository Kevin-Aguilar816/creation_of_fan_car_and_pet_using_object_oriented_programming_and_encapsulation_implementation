from electric_fan.fan_class import Fan
from car.car_class import Car
from pet.pet_class import Pet


def get_pet():
    pet = Pet()
    pet.set_name(input("Enter your pet's name: "))
    pet.set_animal_type(input("Enter your pet's animal type: "))
    pet.set_age(float(input("Enter your pet's age: ")))
    return pet


def car_accelerate(car, fan_one, pet):
    while car.get_speed() != "25 km/h":
        car.accelerate()
        print(
            f"My {my_car.get_year_model()} {my_car.get_make()} has a speed of ({car.get_speed()} km/h)")

    fan_one.set_is_on(True)
    print(f"{pet.get_name()} is enjoying the {fan_one.get_color()} fan at {fan_one.get_speed()} speed while my {my_car.get_year_model()} {my_car.get_make()} is accelerating!")


def car_brake(car, fan_two):
    while car.get_speed() != "0 km/h":
        car.brake()
        print(
            f"My {my_car.get_year_model()} {my_car.get_make()} has a speed of {car.get_speed()} km/h")

    fan_two.set_is_on(False)
    print(f"my {my_car.get_year_model()} {my_car.get_make()} has stopped and my {fan_two.get_color()} fan is now off.")


if __name__ == "__main__":
    my_pet = get_pet()
    my_car = Car(2026, "Ferrarri", 0)
    fan_one = Fan("fast", False, 10.0, "yellow")
    fan_two = Fan("medium", True, 5.0, "blue")

    print(
        f"\n Initial speed of my {my_car.get_year_model()} {my_car.get_make()} is {my_car.get_speed()} km/h")
