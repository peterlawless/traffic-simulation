import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series


"""
Drivers want to go up to 120 km/hr.
The average car is 5 meters long.
Drivers want at least a number of meters equal to their speed in meters/second between them and the next car.
Drivers will accelerate 2 m/s up to their desired speed as long as they have room to do so.
If another car is too close, drivers will match that car's speed until they have room again.
If a driver would hit another car by continuing, they stop.
Drivers will randomly (10% chance each second) slow by 2 m/s.
This section of road is one lane going one way.
"""


class Car:
    def __init__(self, road, length=5, max_speed=120, accel=2, back=0, speed=0):
        self.length = length
        self.max_speed = max_speed
        self.accel = accel
        self.back = back
        self.front = self.back + self.length
        self.road = road
        self.speed = speed

    def drive(self):
        initial_speed = self.speed
        final_speed = self.speed + self.accel
        avg_speed = np.mean([initial_speed, final_speed])

        self.speed = final_speed

        self.back += avg_speed

        """Simulates one second of driving"""
        #if room to accelerate: accelerate
        #if car too close
         #self.position = self.position + (self.speed)
         #self.speed = seconds * self.speed

    def random_slow(self):
        if random.randint(1, 10) == 1:
            self.speed -= 2

    # def dist_to_next_car(self, car_in_front):
    #     return car_in_front.back - self.front

    def can_accel(self, car_in_front):
        return self.dist_to_next_car(car_in_front) > self.speed



class Road:
    def __init__(self, length):
        self.length = length

def main():
    time = 60
    road = Road(1000)
    car1 = Car(road)
    while time > 0:
        car1.drive()
        print("""
time: {},
speed: {}
accel: {}
back: {}
""".format(time, car1.speed, car1.accel, car1.back))
        time -=1


if __name__ == '__main__':
    main()
