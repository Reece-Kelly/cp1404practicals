"""
Estimate time to complete: 40 minutes
Start time: 11:25
Finish time:
"""
VINTAGE_THRESHOLD = 50
CURRENT_YEAR = 2023


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_THRESHOLD
