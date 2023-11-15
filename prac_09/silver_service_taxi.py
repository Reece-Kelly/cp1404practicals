from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness

    def get_fare(self):
        return (self.price_per_km * self.fanciness) * self.current_fare_distance + self.flagfall


