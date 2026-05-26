class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed, is_on, radius, color):
        self.__speed = speed
        self.__is_on = is_on
        self.__radius = radius
        self.__color = color
