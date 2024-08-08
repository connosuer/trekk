import random

class Location:
    def __init__(self, name, country, description, available_jobs):
        self.name = name
        self.country = country
        self.description = description
        self.available_jobs = available_jobs

class LocationManager:
    def __init__(self):
        self.locations = {}
        self.cities = [
            ("New York", "USA"), ("Tokyo", "Japan"), ("London", "UK"), ("Paris", "France"),
            ("Sydney", "Australia"), ("Rio de Janeiro", "Brazil"), ("Cairo", "Egypt"),
            ("Mumbai", "India"), ("Beijing", "China"), ("Moscow", "Russia"),
            ("Cape Town", "South Africa"), ("Toronto", "Canada"), ("Berlin", "Germany"),
            ("Dubai", "UAE"), ("Singapore", "Singapore")
        ]
        self.descriptions = [
            "A bustling metropolis with towering skyscrapers",
            "A historic city with rich cultural heritage",
            "A coastal paradise with beautiful beaches",
            "A technological hub at the forefront of innovation",
            "A charming town with picturesque landscapes"
        ]
        self.jobs = [
            "Teacher", "Software Developer", "Chef", "Journalist", "Doctor",
            "Artist", "Police Officer", "Entrepreneur", "Scientist", "Tour Guide"
        ]

    def generate_random_location(self):
        city, country = random.choice(self.cities)
        description = random.choice(self.descriptions)
        available_jobs = random.sample(self.jobs, 3)
        return Location(city, country, description, available_jobs)

    def get_or_create_location(self, name):
        if name not in self.locations:
            for city, country in self.cities:
                if city == name:
                    self.locations[name] = Location(city, country, random.choice(self.descriptions), random.sample(self.jobs, 3))
                    break
            else:
                # If the city is not in our predefined list, generate a random one
                self.locations[name] = self.generate_random_location()
        return self.locations[name]

    def move_to(self, character, location_name):
        location = self.get_or_create_location(location_name)
        character.location = location_name
        return f"You have moved to {location.name}, {location.country}. {location.description}"

    def list_locations(self):
        return list(self.locations.keys())

    def get_random_location_name(self):
        return random.choice(self.cities)[0]