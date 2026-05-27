from car_class import Car


def car_accelerate(Car):
    for i in range(5):
        Car.accelerate()
        return Car.get_speed()


def car_brake(Car):
    for i in range(5):
        Car.brake()
        return Car.get_speed()
