from electric_fan.fan_class import Fan
from car.car_class import Car
from pet.pet_class import Pet


def get_pet():
    pet = Pet()
    pet.set_name(input("Enter your pet's name: "))
    pet.set_animal_type(input("Enter your pet's animal type: "))
    pet.set_age(float(input("Enter your pet's age: ")))
    return pet


def car_accelerate(Car, Fan, Pet):
    while Car.get_speed() != "25 km/h":
        Car.accelerate()
        print(
            f"\nMy {my_car.get_year_model()} {my_car.get_make()} has a speed of {Car.get_speed()}")

    fan_one.set_is_on(False)
    print(f"\n{my_pet.get_name()} enjoyed the {fan_one.get_color()} fan at {fan_one.get_speed()} speed while my {my_car.get_year_model()} {my_car.get_make()} accelerated!")


def car_brake(Car, Fan):
    while Car.get_speed() != "0 km/h":
        Car.brake()
        print(
            f"\nMy {my_car.get_year_model()} {my_car.get_make()} has a speed of {Car.get_speed()}")

    fan_two.set_is_on(True)
    print(f"\nMy {my_car.get_year_model()} {my_car.get_make()} has stopped and my {fan_two.get_color()} fan is still off.")


if __name__ == "__main__":
    my_pet = get_pet()
    my_car = Car(2026, "Ferrarri", 0)
    fan_one = Fan("fast", True, 10.0, "yellow")
    fan_two = Fan("medium", False, 5.0, "blue")

    print(f"\nHi there! I'm with {my_pet.get_name()}. {my_pet.get_name()} is a {my_pet.get_age()} year-old {my_pet.get_animal_type()}.\nWe have a {my_car.get_year_model()} {my_car.get_make()} that has {fan_one.get_radius()} radius {fan_one.get_color()} fan and {fan_two.get_radius()} radius {fan_two.get_color()} fan that can reach {fan_two.get_speed()} speed.")
    print(
        f"\nThe initial speed of my {my_car.get_year_model()} {my_car.get_make()} is {my_car.get_speed()}")
    print(f"\nThe {fan_one.get_color()} fan is {fan_one.get_is_on()} for {my_pet.get_name()} to enjoy its {fan_one.get_speed()} speed while my {my_car.get_year_model()} {my_car.get_make()} is accelerating.")
    print(
        f"\nThe {fan_two.get_color()} fan is {fan_two.get_is_on()} for me as I am cool myself.")

    car_accelerate(my_car, fan_one, my_pet)
    car_brake(my_car, fan_two)
