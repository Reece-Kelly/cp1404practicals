from car import Car
import random


class UnreliableCar(Car):
    """Subclass of Car Superclass that has reliability attribute."""
    def __init__(self, name, fuel, reliability):
        """Initialise the Unreliable Car object."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance if reliability is greater than random number."""
        random_reliability_number = random.randint(0, 100)
        if random_reliability_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
