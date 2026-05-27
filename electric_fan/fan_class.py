class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed=slow, is_on=False, radius=5.0, color='blue')):
        self.__speed = speed
        self.__is_on = is_on
        self.__radius = radius
        self.__color = color

        def get_speed(self):
        return self.__speed

        def set_speed(self, speed):
        self.__speed = speed
