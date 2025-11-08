from oop_2026.bible.basic.c import Car, Wheel


# install with `poetry add pytest --group dev`

# prompt: for the attached code generate 5 simple (but independent) tests of the change_wheel method:
# (code attached - of class Car and Wheel)

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


# Test 6: Changing wheel with same wheel object (idempotent replacement)
def test_change_wheel_same_object():
    car = Car('TestCar')
    wheel = Wheel('A', 2.5)
    car.change_wheel('LF', wheel)
    result = car.change_wheel('LF', wheel)  # Replace with same object
    assert result == wheel  # Should return the same wheel object
    assert car.get_wheel('LF') == wheel
    assert car.get_wheel('LF') is wheel  # Check object identity


# Test 7: Wheels with identical attributes but different objects
def test_change_wheel_identical_attributes():
    car = Car('TestCar')
    wheel1 = Wheel('B', 3.0)
    wheel2 = Wheel('B', 3.0)  # Same attributes, different object
    car.change_wheel('RF', wheel1)
    result = car.change_wheel('RF', wheel2)
    assert result is wheel1  # Should return first wheel object
    assert result is not wheel2
    assert car.get_wheel('RF') is wheel2  # New wheel is now installed
    assert car.get_wheel('RF') is not wheel1


# Test 8: Using a wheel removed from one position at another position
def test_change_wheel_reuse_removed():
    car = Car('TestCar')
    wheel1 = Wheel('A', 2.5)
    wheel2 = Wheel('B', 3.0)
    car.change_wheel('LF', wheel1)
    car.change_wheel('RR', wheel2)
    removed_wheel = car.change_wheel('LF', wheel2)  # Remove wheel1 from LF, install wheel2
    result = car.change_wheel('RR', removed_wheel)  # Install removed wheel1 at RR
    assert result == wheel2  # wheel2 was at RR
    assert car.get_wheel('LF') == wheel2
    assert car.get_wheel('RR') == removed_wheel
    assert car.get_wheel('RR') == wheel1


# Test 7: Using the same wheel object in multiple locations and replacing one
def test_change_wheel_aliasing_and_replacement():
    car = Car('TrickyCar')
    shared_wheel = Wheel('S', 2.0)
    new_wheel = Wheel('N', 2.1)
    car.change_wheel('LF', shared_wheel)
    car.change_wheel('RF', shared_wheel)
    car.change_wheel('LF', new_wheel)
    # The wheel at RF should still be the original shared_wheel
    assert car.get_wheel('RF') is shared_wheel
    assert car.get_wheel('LF') is new_wheel


# Test 8: Changing a wheel with a non-Wheel object (type flexibility)
def test_change_wheel_with_invalid_object_type():
    car = Car('TrickyCar')
    not_a_wheel = 'Just a string'
    # The method does not enforce the type, so this should not fail
    returned = car.change_wheel('LR', not_a_wheel)
    assert returned is None
    assert car.get_wheel('LR') == not_a_wheel
