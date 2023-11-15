class Band:
    def __init__(self, name: str):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} {[musician for musician in self.musicians]}"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician.play())