class Car:

    def __init__(self, model, make, speed=0):
        self.__year_model = model
        self.__make = make
        self.__speed = speed

    def accelerate(self):
        self.__speed += 5
        return f"{self.__speed} km/h"

    def brake(self):
        self.__speed -= 5
        return f"{self.__speed} km/h"

    def get_speed(self):
        self.__speed = self.__speed
        return f"{self.__speed} km/h"

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make
