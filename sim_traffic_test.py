from nose.tools import raises
from sim_traffic import *


def test_road_prop():
    road = Road(1000, 10)
    assert road.length == 1000
    assert road.num_cars == 10


def test_road_cars():
    road = Road(1000, 10)
    print(road.car_list[0].index)
    assert len(road.car_list) == 10
    assert road.car_list[0].position[0] == 0
    assert road.car_list[0].position[1] == 5
    assert road.car_list[0].speed == 2
    assert road.car_list[0].index == '1'
    assert road.car_list[1].position[0] == 100
    assert road.car_list[1].position[1] == 105
    assert road.car_list[1].index == '2'

    road = Road(500, 20)
    print(road.car_list[0].index)
    assert len(road.car_list) == 10
    assert road.car_list[0].position[0] == 0
    assert road.car_list[0].position[1] == 5
    assert road.car_list[0].speed == 2
    assert road.car_list[0].index == '1'
    assert road.car_list[1].position[0] == 25
    assert road.car_list[1].position[1] == 30
    assert road.car_list[1].index == '2'

@raises(RoadError)
def test_road_cars():
    road = Road(100, 25)


def test_update_position():
    car1 = Car(0, 1000, 1)
    car2 = Car(999, 1000, 2)
    car3 = Car(1003, 1000, 2)

    assert car1.back == 0
    assert car1.front == 5
    assert car2.back == 999
    assert car2.front == 4
    assert car3.back == 3
    assert car3.front == 8


def test_dist_to_car_in_front():
    road = Road(1000, 10)
    assert road.car_list[0].dist_to_car_in_front(road.car_list[1]) == 95

    car3 = Car(500, 1000, 1)
    car4 = Car(5, 1000, 2)
    print(car3.dist_to_car_in_front(car4))
    assert car3.dist_to_car_in_front(car4) == 500

@raises(CrashError)
def test_dist_to_car_in_front_crash_end_of_road():
    car1 = Car(999, 1000, 1)
    car2 = Car(2, 1000, 2)
    car2.dist_to_car_in_front(car2)

@raises(CrashError)
def test_dist_to_car_in_front_crash_touching():
    car1 = Car(0, 1000, 1)
    car2 = Car(5, 1000, 2)
    car1.dist_to_car_in_front(car2)

@raises(CrashError)
def test_dist_to_car_in_front_crash_full_overlap():
    car1 = Car(5, 1000, 1)
    car2 = Car(5, 1000, 2)
    car1.dist_to_car_in_front(car2)


def test_can_accelerate():
    car1 = Car(5, 1000, 1)
    car2 = Car(500, 1000, 2)
    assert car1.can_accelerate(car2)


def test_can_not_accelerate_hit_car():
    car1 = Car(10, 1000, 1)
    car1.speed = 20
    car2 = Car(20, 1000, 2)
    assert car1.can_accelerate(car2) == False


def test_can_not_accelerate_too_fast():
    car1 = Car(10, 1000, 1)
    car1.speed = 120
    car2 = Car(600, 1000, 2)
    assert car1.can_accelerate(car2) == False


def test_gotta_back_off():
    car1 = Car(10, 1000, 1)
    car1.speed = 5
    car2 = Car(18, 1000, 2)
    assert car1.gotta_back_off(car2)

def test_dont_gotta_back_off():
    car1 = Car(10, 1000, 1)
    car1.speed = 5
    car2 = Car(25, 1000, 2)
    assert car1.gotta_back_off(car2) == False


def test_drive():
    car1 = Car(10, 1000, 1)
    car2 = Car(25, 1000, 2)
    car1.drive(1, car2)
    car2.drive(1, car1)

    car1_expected_hist = pd.DataFrame({'speed': [2, 4],
                                       'back': [10, 12],
                                       'time': [0, 1],
                                       'carID': [1, 1]})

    car2_expected_hist = pd.DataFrame({'speed': [2, 4],
                                       'back': [25, 27],
                                       'time': [0, 1],
                                       'carID': [2, 2]})
    print(car1.hist)
    print(car1_expected_hist)
    print(car2.hist)

    assert car1.hist.equals(car1_expected_hist)
    assert car2.hist.equals(car2_expected_hist)
