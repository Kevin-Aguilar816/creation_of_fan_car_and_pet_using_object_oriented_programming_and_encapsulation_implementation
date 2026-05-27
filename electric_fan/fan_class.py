class Fan:
    slow = 1
    medium = 2
    fast = 3
    speed_values = {1: 'slow', 2: 'medium', 3: 'fast'}

    def __init__(self, speed=1, is_on=False, radius=5.0, color='blue'):
        self.__speed = speed
        self.__is_on = is_on
        self.__radius = radius
        self.__color = color

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return (f"{self.__radius} cm")

    def get_color(self):
        return self.__color

    def get_is_on(self):
        return self.__is_on

    def set_speed(self, speed):
        self.__speed = speed

    def set_is_on(self, is_on):
        self.__is_on = is_on

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color
