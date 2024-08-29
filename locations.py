import random
import numpy as np
from faker import Faker

fake = Faker()

class Location:
    def __init__(self, name, country, traits):
        self.name = name
        self.country = country
        self.traits = traits
        self.description = self.generate_description()
        self.people = [fake.name() for _ in range(random.randint(3, 10))]
        self.objects = [fake.word() for _ in range(random.randint(5, 15))]

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

class DynamicWorld:
    def __init__(self):
        self.locations = {}
        self.faker = Faker()

    def get_or_create_location(self, name=None):
        if name is None:
            name = self.faker.city()
        
        if name not in self.locations:
            country = self.faker.country()
            traits = np.random.rand(5)  # Random traits for the location
            self.locations[name] = Location(name, country, traits)
        
        return self.locations[name]

    def find_nearest_location(self, current_location):
        if not self.locations:
            return None
        
        current_traits = self.locations[current_location].traits
        nearest = min(self.locations.values(), key=lambda x: np.linalg.norm(x.traits - current_traits))
        return nearest.name if nearest.name != current_location else None

    def generate_travel_event(self, from_location, to_location):
        events = [
            f"You take a scenic route from {from_location} to {to_location}.",
            f"Your journey from {from_location} to {to_location} is filled with unexpected detours.",
            f"You meet interesting fellow travelers on your way from {from_location} to {to_location}.",
            f"The trip from {from_location} to {to_location} is surprisingly smooth and uneventful.",
            f"You experience culture shock as you travel from {from_location} to {to_location}."
        ]
        return random.choice(events)