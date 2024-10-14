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
        self.description = self.generate_description()
        self.people = [faker.name() for _ in range(random.randint(3, 10))]
        self.objects = [faker.word() for _ in range(random.randint(5, 15))]

    def generate_description(self):
        adjectives = ["bustling", "quiet", "historic", "futuristic", "mysterious", "charming", "gritty", "elegant", "vibrant", "serene"]
        features = ["streets", "architecture", "atmosphere", "skyline", "culture", "landscape", "people", "energy", "traditions", "innovations"]
        return f"A {random.choice(adjectives)} place known for its {random.choice(features)}."

    def get_random_event(self):
        events = [
            "A street performer catches your eye.",
            "You overhear an intriguing conversation.",
            "A local festival is in full swing.",
            "You stumble upon a hidden gem of a cafe.",
            "A sudden weather change surprises everyone.",
            f"You bump into {random.choice(self.people)}.",
            f"You find a peculiar {random.choice(self.objects)} on the ground.",
        ]
        return random.choice(events)

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

    def find_nearest_location(self, current_location):
        if len(self.locations) < 2:
            return None
        locations = list(self.locations.values())
        return random.choice([loc for loc in locations if loc.name != current_location]).name

    def generate_travel_event(self, from_location, to_location):
        events = [
            f"You take a scenic route from {from_location} to {to_location}.",
            f"Your journey from {from_location} to {to_location} is filled with unexpected detours.",
            f"You meet interesting fellow travelers on your way from {from_location} to {to_location}.",
            f"The trip from {from_location} to {to_location} is surprisingly smooth and uneventful.",
            f"You experience culture shock as you travel from {from_location} to {to_location}."
        ]
        return random.choice(events)