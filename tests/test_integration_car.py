from lib.car import Car
from lib.tyre import Tyre

def test_has_list_of_tyre_objects():
    car = Car()
    left_front_tyre = Tyre('left front', '30', '25', '01/01/26')
    right_front_tyre = Tyre('right front', '33', '27', '01/01/26')
    car.add_tyre(left_front_tyre)
    car.add_tyre(right_front_tyre)
    assert car.list_of_tyres == [left_front_tyre, right_front_tyre]

def test_car_can_add_readings_to_tyres():
    car = Car()
    left_front_tyre = Tyre('left front', '30', '25', '01/01/26')
    right_front_tyre = Tyre('right front', '33', '27', '01/01/26')
    car.add_tyre(left_front_tyre)
    car.add_tyre(right_front_tyre)

    left_front_tyre.add_reading('25', '20', '03/03/26')
    assert car.list_tyre_pos_and_readings() == f'{left_front_tyre.position} - pressure: {left_front_tyre.pressure}, tread: {left_front_tyre.tread}, date: {left_front_tyre.date}\n{right_front_tyre.position} - pressure: {right_front_tyre.pressure}, tread: {right_front_tyre.tread}, date: {right_front_tyre.date}\n'
    