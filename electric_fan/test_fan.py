from fan_class import Fan


def test_fan_one(Fan):
    fan_one = Fan()
    fan_one.set_speed('fast')
    fan_one.set_is_on(True)
    fan_one.set_radius(10.0)
    fan_one.set_color('yellow')
    return fan_one


def test_fan_two(Fan):
    fan_two = Fan()
    fan_two.set_speed('medium')
    fan_two.get_is_on
    fan_two.get_color
    fan_two.get_radius
    return fan_two


if __name__ == "__main__":
    fan_one = test_fan_one(Fan)
    fan_two = test_fan_two(Fan)
print(f"Fan one speed: {fan_one.get_speed()}\n Fan one radius: {fan_one.get_radius()}\n Fan one color: {fan_one.get_color()}\n Fan one is on: {fan_one.get_is_on()}")
print(f"Fan two speed: {fan_two.get_speed()}\n Fan two radius: {fan_two.get_radius()}\n Fan two color: {fan_two.get_color()}\n Fan two is on: {fan_two.get_is_on()}")
