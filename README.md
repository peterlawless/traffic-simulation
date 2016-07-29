#traffic-simulation

## Synopsis

The purpose of this repository is to analyze the behavior of drivers on a new
road to determine the optimal speed limits.

Assume we have a 1 kilometer section of road being built and do not know what
the speed limit needs to be. The code in sim_traffic.py simulates 1 kilometer of
road and the behavior of cars driving on that road. Even though this road is not
circular, it is treated as such in order to generate a continuous flow of traffic.

### Assumptions:

* Drivers want to go up to 120 km/hr.
* The average car is 5 meters long.
* Drivers want at least a number of meters equal to their speed in meters/second
between them and the next car.
* Drivers will accelerate 2 m/s up to their desired speed as long as they have
room to do so.
* If another car is too close, drivers will match that car's speed until they
have room again.
* If a driver would hit another car by continuing, they stop.
* Drivers will randomly (10% chance each second) slow by 2 m/s.
* This section of road is one lane going one way.
* Given all this information, create a simulation of traffic on this road.

The optimal speed limit is one standard deviation above the mean speed.
For ease of drivers, this will be rounded down to an integer.

The final report in the traffic-simulation.ipynb file has a graph of traffic
over time, showing traffic jams, as well as our recommendation for the speed
limit.
