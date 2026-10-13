from lib.car import Car

def test_car_has_an_empty_list_of_tyres():
    car = Car()
    assert car.list_of_tyres == []

    