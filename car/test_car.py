from car_class import Car


def car_accelerate(car):
    while car.get_speed() != "25 km/h":
        car.accelerate()
        print(
            f"My {my_car.get_year_model()} {my_car.get_make()} has a speed of: {car.get_speed()}")


def car_brake(car):
    while car.get_speed() != "0 km/h":
        car.brake()
        print(
            f"My {my_car.get_year_model()} {my_car.get_make()} has a speed of: {car.get_speed()}")


if __name__ == "__main__":
    my_car = Car(2026, 'Ferrarri', 0)

car_accelerate(my_car)
car_brake(my_car)
