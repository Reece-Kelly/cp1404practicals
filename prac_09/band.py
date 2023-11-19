class Band:
    def __init__(self, name: str):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician.play())