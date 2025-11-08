from oop_2026.bible.basic.c import Car, Wheel


# install with `poetry add pytest --group dev`

def test_works():
    assert True


# Test 1: Adding a wheel to an empty position returns None
def test_change_wheel_empty_position():
    car = Car('TestCar')
    wheel = Wheel('A', 2.5)
    result = car.change_wheel('LF', wheel)
    assert result is None
    assert car.get_wheel('LF') == wheel


# Test 2: Replacing an existing wheel returns the old wheel
def test_change_wheel_replace_existing():
    car = Car('TestCar')
    old_wheel = Wheel('A', 2.5)
    new_wheel = Wheel('B', 3.0)
    car.change_wheel('RF', old_wheel)
    result = car.change_wheel('RF', new_wheel)
    assert result == old_wheel
    assert car.get_wheel('RF') == new_wheel


# Test 3: Changing wheel with invalid position raises ValueError
def test_change_wheel_invalid_position():
    car = Car('TestCar')
    wheel = Wheel('C', 3.5)
    try:
        car.change_wheel('INVALID', wheel)
        assert False, 'Should have raised ValueError'
    except ValueError as e:
        assert 'Invalid wheel position' in str(e)


# Test 4: Changing wheels at different positions independently
def test_change_wheel_multiple_positions():
    car = Car('TestCar')
    wheel_lf = Wheel('A', 2.0)
    wheel_rr = Wheel('B', 2.5)
    result_lf = car.change_wheel('LF', wheel_lf)
    result_rr = car.change_wheel('RR', wheel_rr)
    assert result_lf is None
    assert result_rr is None
    assert car.get_wheel('LF') == wheel_lf
    assert car.get_wheel('RR') == wheel_rr


# Test 5: Replacing wheel multiple times at same position
def test_change_wheel_multiple_replacements():
    car = Car('TestCar')
    wheel1 = Wheel('A', 2.0)
    wheel2 = Wheel('B', 2.5)
    wheel3 = Wheel('C', 3.0)
    car.change_wheel('LR', wheel1)
    result2 = car.change_wheel('LR', wheel2)
    result3 = car.change_wheel('LR', wheel3)
    assert result2 == wheel1
    assert result3 == wheel2
    assert car.get_wheel('LR') == wheel3
