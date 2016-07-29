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


"""
From: http://statweb.stanford.edu/~owen/mc/Ch-intro.pdf
The rules for Nagel-Schreckenberg traffic are as follows. At each stage
of the simulation, every car goes through the following four steps.
1. First, if its velocity is below vmax, it increases its velocity by one unit.
The drivers are eagerto move ahead.
2. Second, it checks the distance to the car in front of it. If that
    distance is d spaces and the car has velocity v > d then it reduces its velocity
to d − 1 in order to avoid collision.
3. Third, if the velocity is positive then with
probability p it reduces velocity by 1 unit. This is the key step which models
random driver behavior.
4. At the fourth step, the car moves ahead by v units to
complete the stage. These four steps take place in parallel for all N vehicles.
Let x ∈ {0, 1, . . . , M − 1} be the position of a car, v its velocity, and d be
the distance to the car ahead. The update for this car is:
    v ← min(v + 1, vmax)
    v ← min(v, d − 1)
    v ← max(0, v − 1) with probability p
    x ← x + v.
At the last step, if x + v > M then x ← x + v − M. Similarly, for the car with
the largest x, the value of d is M plus the smallest x, minus the largest x.
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
""" v ← min(v + 1, vmax)
    v ← min(v, d − 1)
    v ← max(0, v − 1) with probability p
    x ← x + v.
"""

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

         self.end_of_road()

    def random_slow(self):
        if random.randint(1, 10) == 1:
            self.speed -= 2

    def dist_to_next_car(self, car_in_front):
        return car_in_front.back - self.front

    def end_of_road(self):
        """To be performed at end of each drive call"""
        if self.front > self.road.length:
            self.font = self.front - self.road.length
        if self.back > self.road.length:
            self.back = self.back - self.road.length

    def can_accel(self, car_in_front):
        return self.dist_to_next_car(car_in_front) > self.speed



class Road:
    def __init__(self, length, cars=[]):
        self.length = length
        self.cars = cars

    def add_car(self, car):
        self.cars.append(car)

    def count_crashes(self):
        """This function should run after all the cars have moved."""
        crashes = 0
        for i in range(len(cars)):
            if crashes[i].front >= crashes[i + 1].back:
                crashes += 1
        return crashes





def main():
    time = 60
    crash_count = 0
    road = Road(1000) #
    car1 = Car(road)
    while time > 0:
        # TODO: Once function is finalized: this will be a loop through the Road object's array of cars
        car1.drive()
        print("""
time: {},
speed: {}
accel: {}
back: {}
""".format(time, car1.speed, car1.accel, car1.back))
        time -= 1


if __name__ == '__main__':
    main()
