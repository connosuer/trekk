import random
from faker import Faker

faker = Faker()

class Location:
    def __init__(self, name, country, population, climate, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.climate = climate
        self.landmarks = landmarks

class WorldGenerator:
    def __init__(self):
        self.locations = {}

    def generate_location(self):
        name = faker.city()
        country = faker.country()
        population = random.randint(1000, 10000000)
        climate = random.choice(["tropical", "dry", "temperate", "continental", "polar"])
        landmarks = [faker.company() for _ in range(random.randint(1, 5))]
        return Location(name, country, population, climate, landmarks)

    def get_or_create_location(self, name=None):
        if name is None or name not in self.locations:
            location = self.generate_location()
            self.locations[location.name] = location
            return location
        return self.locations[name]

