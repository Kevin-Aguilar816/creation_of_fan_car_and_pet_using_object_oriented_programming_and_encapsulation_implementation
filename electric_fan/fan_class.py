class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed, is_on, radius, color):
        self.__speed = speed
        self.__is_on = is_on
        self.__radius = radius
        self.__color = color

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed
