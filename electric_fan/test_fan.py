from fan_class import Fan


def test_fan():
    fan_one = Fan(fan.fast, False, 10.0, 'yellow')
    fan_two = Fan(fan.medium, True,  5.0, 'blue')
