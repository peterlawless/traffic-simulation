import numpy as np
import pandas as pd
import random


class RoadError(Exception):
    pass


class CrashError(Exception):
    pass


class Car:
    def __init__(self, pos, road_len, index=1, length=5, max_speed=120):
        self.road_len = road_len
        self.length = length
        self.pos = pos
        # position = [back, front], cars are assumed to have 5m length
        self.update_position()
        self.index = index
        # self.car_in_front = None
        self.speed = 2
        self.max_speed = max_speed
        self.v = [self.speed]  # list of speed points
        self.x = [self.pos]  # list of position points
        self.hist = pd.DataFrame({'speed': [self.speed],
                                  'back': [self.back],
                                  'time': [0],
                                  'carID': [self.index]})

    def update_position(self):
        self.back = self.pos % self.road_len
        self.front = (self.pos + self.length) % self.road_len
        # self.position = [self.pos % self.road_len,
        #                  (self.pos + self.length) % self.road_len]

    def dist_to_car_in_front(self, cif):

        #dist_apart = cif.position[0] - self.position[1]:

        if self.front < cif.back:
            return cif.back - self.front
        elif self.front - cif.back > 2 * self.length:
            return cif.back + self.road_len - self.front
        # This else statement considers that when a car loops back to the
        # beginning of the road, the difference between the car in front will
        # be a negative number
        else:
            raise CrashError("Oh the humanity! {} crashed into {}.".format(self.index, cif.index))


    # Drivers want at least a number of meters equal to their speed in
    # meters/second between them and the next car.
    # Drivers will accelerate 2 m/s up to their desired speed as long as they
    # have room to do so.
    def can_accelerate(self, cif):
        return (self.dist_to_car_in_front(cif) >= self.speed
                and self.speed < self.max_speed)

    # Drivers will randomly (10% chance each second) slow by 2 m/s.
    def is_shitty_driver(self):
        return (random.randint(1, 10) == 1 and self.speed >= 2)

    # If another car is too close, drivers will match that car's speed until
    # they have room again.
    def gotta_back_off(self, cif):
        return self.dist_to_car_in_front(cif) < self.speed

    def drive(self, time, car_in_front):
        if self.is_shitty_driver():
            self.speed -= 2
        if self.can_accelerate(car_in_front):
            self.speed += 2
        if self.gotta_back_off(car_in_front):
            self.speed = car_in_front.speed

        self.v.append(self.speed)
        self.pos += self.v[-2]
        self.update_position()
        self.x.append(self.pos)
        new_position = pd.DataFrame({'speed': [self.speed],
                                     'back': [self.back],
                                     'time': [time],
                                     'carID': [self.index]})
        self.hist = self.hist.append(new_position).reset_index(drop=True)


class Road:
    def __init__(self, length=1000, num_cars=30):
        self.length = length
        self.num_cars = num_cars
        self.car_list = []
        pos = 0
        for idx in range(self.num_cars):
            self.car_list.append(Car(pos, self.length, idx + 1))
            if len(self.car_list) > 1:
                self.car_list[-2].car_in_front = self.car_list[-1]
            pos += self.length / self.num_cars
        # return car_list

        if sum([car.length for car in self.car_list]) > self.length:
            raise RoadError("Not enough room for the cars!")



def main():
    road = Road(1000, 30)
    # print([car_list[0].pos[0], car_list[1].pos[0], car_list[2].pos[0]])

if __name__ == '__main__':
    main()
