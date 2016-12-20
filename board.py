import numpy as np

l = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

class Board():
    def __init__(self):
        self.resouce_positions = []
        self.generate_initial_positions()
        self.settlements = []
        self.roads = []
        self.cities = []

    """ Initialize the board positions """
    def generate_initial_positions(self):
        brick = ["brick"] * 3
        ore = ["ore"] * 3
        wheat = ["wheat"] * 4
        wood = ["wood"] * 4
        sheep = ["sheep"] * 4
        desert = ["desert"]
        resources = np.concatenate((brick, ore, wheat, wood, sheep, desert))
        np.random.shuffle(resources)

        index = 0
        for resource in resources:
            if resource != "desert":
                self.resouce_positions.append((resource, l[index]))
                index = index + 1
            else:
                self.resouce_positions.append((resource, 0))

b = Board()
print b.resouce_positions
