from fan_class import Fan


def test_fan(Fan):
    fan_one = Fan()
    fan_one.set_speed('fast')
    fan_one.set_is_on(True)
    fan_one.set_radius(10.0)
    fan_one.set_color('yellow')
    return fan_one


if __name__ == "__main__":
    fan_one = test_fan(Fan)

print(f"Fan one speed: {fan_one.get_speed()}\n Fan one radius: {fan_one.get_radius()}\n Fan one color: {fan_one.get_color()}\n Fan one is on: {fan_one.get_is_on(True)}")
