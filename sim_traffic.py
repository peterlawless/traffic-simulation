import numpy as np
import random


class Car:
    def __init__(self, pos, road_len):
        self.road_length = road_len
        self.pos = pos
        self.position = np.array([self.pos % self.road_len, (self.pos + 5) % self.road_len])
        self.car_in_front = None
        self.accel = 0
        self.speed = 0
        self.a = []  # list of acceleration points
        self.v = []  # list of speed points
        self.x = []  # list of position points

    def dist_to_car_in_front(self):
        if self.car_in_front.pos[0] > self.pos[1]:
            return self.car_in_front.pos[0] - self.pos[1]
        # This else statement considers that when a car loops back to the
        # beginning of the road, the difference between the car in front will
        # be a negative number
        else:
            return (self.car_in_front.pos[0] + self.road_len) - self.pos[1]

    # Drivers want at least a number of meters equal to their speed in
    # meters/second between them and the next car.
    # Drivers will accelerate 2 m/s up to their desired speed as long as they
    # have room to do so.
    def can_accelerate(self):
        return self.dist_to_car_in_front >= self.speed

    # Drivers will randomly (10% chance each second) slow by 2 m/s.
    def is_shitty_driver(self):
        return random.randint(1, 10) == 1

    # If another car is too close, drivers will match that car's speed until
    # they have room again.
    def gotta_back_off(self):
        return self.dist_to_car_in_front < self.speed

    def drive(self, time=60):
        for _ in range(0, time):
            if self.is_shitty_driver():
                self.accel -= 2
            elif self.can_accelerate():
                self.accel += 2
            elif self.gotta_back_off():
                self.accel -= 2
            else:
                pass
        pass


class Road:
    def __init__(self, length=1000, num_cars=30):
        self.length = length
        self.num_cars = num_cars

    def populate_road(self):
        self.car_list = []
        pos = 0
        for _ in range(self.num_cars):
            self.car_list.append(Car(pos, self.length))
            if len(self.car_list) > 1:
                self.car_list[-2].car_in_front = self.car_list[-1]
            pos += self.length / self.num_cars
        # return car_list


def main():
    road = Road(1000, 30)
    road.populate_road()
    # print([car_list[0].pos[0], car_list[1].pos[0], car_list[2].pos[0]])


if __name__ == '__main__':
    main()
