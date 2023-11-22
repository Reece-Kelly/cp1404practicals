class Band:
    def __init__(self, name: str):
        """Initialise Band object."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string of a band name, musicians, and instruments."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of the musicians in a band playing their first instrument."""
        for musician in self.musicians:
            print(musician.play())