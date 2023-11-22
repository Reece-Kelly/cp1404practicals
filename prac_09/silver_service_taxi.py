from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Subclass of Taxi that has fanciness attribute."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise Silver Service Taxi object."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price of the taxi trip with the added flagfall amount."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Taxi but with flagfall amount."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"
